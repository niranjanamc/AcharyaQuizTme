import React, { useState, useEffect } from 'react';
import { Check, X, ArrowRight, Lightbulb } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';

const QuizComponent = ({ questionData, onAnswer, language }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [showReasoning, setShowReasoning] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);

  // questionData is now expected to be q[language] directly: { question, options, answer, reasoning }

  useEffect(() => {
    // Reset state when new question loads
    setSelectedOption(null);
    setShowReasoning(false);
    setIsCorrect(false);
  }, [questionData]);

  if (!questionData) return <div>Loading...</div>;

  const handleSubmit = (opt) => {
    soundEngine.playClick();
    setSelectedOption(opt);
    const correct = opt === questionData.answer;
    setIsCorrect(correct);
    setShowReasoning(true);
  };

  const handleNext = () => {
    soundEngine.playClick();
    setShowReasoning(false);
    onAnswer(isCorrect); // Tells parent to update score/lives and give next Q
  };

  const labels = {
    reasoning: language === 'kn' ? 'ಕಾರಣ' : 'Reasoning',
    correct: language === 'kn' ? 'ಸರಿ!' : 'Correct!',
    wrong: language === 'kn' ? 'ತಪ್ಪು!' : 'Incorrect!',
    next: language === 'kn' ? 'ಮುಂದಿನ ಪ್ರಶ್ನೆ' : 'Next Question'
  };

  return (
    <div style={{
      backgroundColor: 'rgba(255, 255, 255, 0.95)',
      padding: '20px',
      borderRadius: '20px',
      boxShadow: 'var(--shadow-md)',
      color: 'var(--text-dark)',
      position: 'relative'
    }}>
      <h2 style={{ fontSize: '1.4rem', marginBottom: '20px', lineHeight: '1.4' }}>
        {questionData.question}
      </h2>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {questionData.options.map((opt, idx) => {
          let btnBg = '#f0f0f0';
          let btnColor = 'var(--text-dark)';
          
          if (showReasoning) {
            if (opt === questionData.answer) {
              btnBg = '#06D6A0'; // Green for correct
              btnColor = 'white';
            } else if (opt === selectedOption && opt !== questionData.answer) {
              btnBg = '#EF476F'; // Red for wrong selected
              btnColor = 'white';
            }
          } else if (opt === selectedOption) {
            btnBg = 'var(--tuk-yellow)';
          }

          return (
            <button
              key={idx}
              disabled={showReasoning}
              onClick={() => handleSubmit(opt)}
              style={{
                padding: '15px',
                borderRadius: '10px',
                border: '2px solid transparent',
                backgroundColor: btnBg,
                color: btnColor,
                fontSize: '1.1rem',
                fontWeight: '600',
                cursor: showReasoning ? 'default' : 'pointer',
                textAlign: 'left',
                transition: 'all 0.2s',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                boxShadow: showReasoning ? 'none' : '0 4px 6px rgba(0,0,0,0.05)'
              }}
            >
              {opt}
              {showReasoning && opt === questionData.answer && <Check size={20} />}
              {showReasoning && opt === selectedOption && opt !== questionData.answer && <X size={20} />}
            </button>
          );
        })}
      </div>

      {showReasoning && (
        <div style={{
          marginTop: '20px',
          padding: '15px',
          backgroundColor: isCorrect ? 'rgba(6, 214, 160, 0.1)' : 'rgba(239, 71, 111, 0.1)',
          borderRadius: '10px',
          borderLeft: `5px solid ${isCorrect ? '#06D6A0' : '#EF476F'}`,
          animation: 'fadeIn 0.5s'
        }}>
          <h3 style={{ display: 'flex', alignItems: 'center', gap: '5px', color: isCorrect ? '#06D6A0' : '#EF476F', margin: '0 0 10px 0' }}>
            {isCorrect ? <Check size={20}/> : <X size={20}/>} 
            {isCorrect ? labels.correct : labels.wrong}
          </h3>
          <p style={{ margin: '0 0 15px 0', fontSize: '0.95rem', lineHeight: '1.5' }}>
            <strong><Lightbulb size={16} style={{display: 'inline', verticalAlign: 'text-bottom'}}/> {labels.reasoning}:</strong> {questionData.reasoning}
          </p>
          <button 
            className="btn btn-secondary" 
            onClick={handleNext}
            style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '10px' }}
          >
            {labels.next} <ArrowRight size={20} />
          </button>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
