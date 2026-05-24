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

const GameArea = ({ level, selectedChapters, language, onCorrect, onWrong, onLevelUp, onExhausted }) => {
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

    if (!selectedChapters || selectedChapters.length === 0) {
      if (isMounted) {
        setError("No chapters selected.");
        setLoading(false);
      }
      return;
    }

    // Load ALL selected chapters in parallel
    const loadPromises = selectedChapters.map(ch => 
      import(`../data/questions/${ch.classId}/${ch.subjectId}/${ch.chapterId}.json`)
        .then(module => module.default || module)
        .catch(err => {
          console.warn(`Failed to load ${ch.chapterId}:`, err);
          return []; // Return empty array for missing chapters so Promise.all doesn't fail
        })
    );

    Promise.all(loadPromises).then((results) => {
      if (isMounted) {
        // Flatten the array of arrays
        const mergedQuestions = results.flat();
        
        if (mergedQuestions.length === 0) {
          setError(`Coming Soon! Add questions via CMS.`);
        } else {
          setQuestions(mergedQuestions);
        }
        setLoading(false);
      }
    });

    return () => { isMounted = false; };
  }, [selectedChapters]);

  useEffect(() => {
    if (questions.length > 0 && !loading) {
      pickNextQuestion(seenQuestions);
    }
  }, [questions, loading, level]);

  const pickNextQuestion = (currentSeen = seenQuestions) => {
    if (questions.length === 0) return;

    let suitableQs = questions.filter(q => q.difficulty === level);
    
    // If no questions exist for this exact level, check if we've gone beyond max
    if (suitableQs.length === 0) {
      const maxDiff = Math.max(...questions.map(q => q.difficulty));
      if (level > maxDiff) {
        onExhausted();
        return;
      }
    }

    let unseenQs = suitableQs.filter(q => !currentSeen.has(q.id));

    if (unseenQs.length === 0) {
      const maxDiff = Math.max(...questions.map(q => q.difficulty));
      if (level < maxDiff) {
        onLevelUp();
        return; // useEffect will re-run when level changes
      } else {
        onExhausted();
        return;
      }
    }

    const randomQ = unseenQs[Math.floor(Math.random() * unseenQs.length)];
    setCurrentQuestion(randomQ);
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
          questionData={{ ...currentQuestion[language], type: currentQuestion.type }} 
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
