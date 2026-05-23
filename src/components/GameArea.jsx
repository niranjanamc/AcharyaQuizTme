import React, { useState, useEffect } from 'react';
import QuizComponent from './QuizComponent';
import { Loader2 } from 'lucide-react';

const FloatingAnimation = ({ type, x, y, onComplete }) => {
  const isPositive = type === 'positive';
  return (
    <div 
      onAnimationEnd={onComplete}
      style={{
        position: 'absolute',
        left: x,
        top: y,
        color: isPositive ? '#06D6A0' : '#EF476F',
        fontSize: '2rem',
        fontWeight: 'bold',
        textShadow: '1px 2px 4px rgba(0,0,0,0.3)',
        animation: 'floatUp 1s ease-out forwards',
        pointerEvents: 'none',
        zIndex: 100
      }}
    >
      {isPositive ? '+SCORE' : '-1 ♥'}
      <style>{`
        @keyframes floatUp {
          0% { transform: translateY(0) scale(1); opacity: 1; }
          100% { transform: translateY(-50px) scale(1.5); opacity: 0; }
        }
      `}</style>
    </div>
  );
};

const GameArea = ({ level, classId, subjectId, chapterId, language, onCorrect, onWrong }) => {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [seenQuestions, setSeenQuestions] = useState(new Set());
  const [animations, setAnimations] = useState([]);

  useEffect(() => {
    let isMounted = true;
    setLoading(true);
    setError(null);

    // Dynamically import the json file for the chapter
    import(`../data/questions/${classId}/${subjectId}/${chapterId}.json`)
      .then((module) => {
        if (isMounted) {
          setQuestions(module.default || module);
          setLoading(false);
        }
      })
      .catch((err) => {
        console.error("Failed to load questions:", err);
        if (isMounted) {
          setError(`Coming Soon! Add questions via CMS.`);
          setLoading(false);
        }
      });

    return () => { isMounted = false; };
  }, [classId, subjectId, chapterId]);

  useEffect(() => {
    if (questions.length > 0 && !loading) {
      pickNextQuestion(seenQuestions);
    }
  }, [questions, loading, level]);

  const pickNextQuestion = (currentSeen = seenQuestions) => {
    // 1. Filter by level/difficulty
    let suitableQs = questions.filter(q => q.difficulty === level);
    
    // Fallback if level exceeds max difficulty
    if (suitableQs.length === 0) {
      const maxDiff = Math.max(...questions.map(q => q.difficulty));
      suitableQs = questions.filter(q => q.difficulty === maxDiff);
    }

    // 2. Filter out seen questions
    let unseenQs = suitableQs.filter(q => !currentSeen.has(q.id));

    // 3. Reset seen pool for this difficulty if we've exhausted them all
    if (unseenQs.length === 0) {
      const qsToReset = suitableQs.map(q => q.id);
      const newSeen = new Set(currentSeen);
      qsToReset.forEach(id => newSeen.delete(id));
      setSeenQuestions(newSeen);
      unseenQs = suitableQs;
    }

    if (unseenQs.length > 0) {
      const randomQ = unseenQs[Math.floor(Math.random() * unseenQs.length)];
      setCurrentQuestion(randomQ);
    } else {
      setError("No questions found for this subject.");
    }
  };

  const handleAnswer = (isCorrect) => {
    let newSeen = seenQuestions;
    if (currentQuestion) {
      newSeen = new Set(seenQuestions);
      newSeen.add(currentQuestion.id);
      setSeenQuestions(newSeen);
    }

    // Add animation
    const newAnim = {
      id: Date.now(),
      type: isCorrect ? 'positive' : 'negative',
      x: '50%',
      y: '40%'
    };
    setAnimations(prev => [...prev, newAnim]);

    if (isCorrect) {
      onCorrect();
    } else {
      onWrong();
    }
    pickNextQuestion(newSeen);
  };

  const removeAnimation = (id) => {
    setAnimations(prev => prev.filter(a => a.id !== id));
  };

  if (loading) {
    return (
      <div style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', color: 'white' }}>
        <Loader2 className="animate-spin" size={48} />
      </div>
    );
  }

  if (error) {
    return <div style={{ flex: 1, color: 'white', padding: '20px', textAlign: 'center' }}>{error}</div>;
  }

  return (
    <div style={{ 
      flex: 1, 
      padding: '20px', 
      overflowY: 'auto',
      display: 'flex',
      flexDirection: 'column',
      position: 'relative'
    }}>
      {animations.map(anim => (
        <FloatingAnimation 
          key={anim.id} 
          type={anim.type} 
          x={anim.x} 
          y={anim.y} 
          onComplete={() => removeAnimation(anim.id)} 
        />
      ))}

      {currentQuestion && currentQuestion[language] ? (
        <QuizComponent 
          questionData={currentQuestion[language]} 
          language={language}
          onAnswer={handleAnswer} 
        />
      ) : (
        <div style={{ color: 'white', textAlign: 'center' }}>Loading question data...</div>
      )}
    </div>
  );
};

export default GameArea;
