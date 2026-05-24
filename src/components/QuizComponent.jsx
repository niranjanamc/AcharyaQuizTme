import React, { useState, useEffect } from 'react';
import { Check, X, ArrowRight, Lightbulb } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';

const QuizComponent = ({ questionData, onAnswer, language }) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [selectedMatches, setSelectedMatches] = useState({});
  const [showReasoning, setShowReasoning] = useState(false);
  const [isCorrect, setIsCorrect] = useState(false);
  const [isPartiallyCorrect, setIsPartiallyCorrect] = useState(false);
  const [shuffledRights, setShuffledRights] = useState([]);

  const qType = questionData?.type || 'single';

  useEffect(() => {
    setSelectedOption(null);
    setSelectedOptions([]);
    setSelectedMatches({});
    setShowReasoning(false);
    setIsCorrect(false);
    setIsPartiallyCorrect(false);

    if (qType === 'match' && questionData.pairs) {
      const rights = questionData.pairs.map(p => p.right);
      setShuffledRights(rights.sort(() => Math.random() - 0.5));
    }
  }, [questionData, qType]);

  if (!questionData) return <div>Loading...</div>;

  const handleSingleSubmit = (opt) => {
    soundEngine.playClick();
    setSelectedOption(opt);
    const correct = String(opt).trim() === String(questionData.answer).trim();
    setIsCorrect(correct);
    setShowReasoning(true);
  };

  const handleMultipleToggle = (opt) => {
    if (showReasoning) return;
    setSelectedOptions(prev => 
      prev.includes(opt) ? prev.filter(o => o !== opt) : [...prev, opt]
    );
  };

  const handleMultipleSubmit = () => {
    soundEngine.playClick();
    const correctAnswers = questionData.answer || [];
    const correct = selectedOptions.length === correctAnswers.length &&
                    selectedOptions.every(val => correctAnswers.includes(val));
    const partial = !correct && selectedOptions.some(val => correctAnswers.includes(val));
    setIsCorrect(correct);
    setIsPartiallyCorrect(partial);
    setShowReasoning(true);
  };

  const handleMatchChange = (left, rightValue) => {
    if (showReasoning) return;
    setSelectedMatches(prev => ({ ...prev, [left]: rightValue }));
  };

  const handleMatchSubmit = () => {
    soundEngine.playClick();
    let correct = true;
    for (let pair of questionData.pairs) {
      if (selectedMatches[pair.left] !== pair.right) {
        correct = false;
        break;
      }
    }
    setIsCorrect(correct);
    setShowReasoning(true);
  };

  const handleNext = () => {
    soundEngine.playClick();
    setShowReasoning(false);
    onAnswer(isCorrect);
  };

  const labels = {
    reasoning: language === 'kn' ? 'ಕಾರಣ' : 'Reasoning',
    correct: language === 'kn' ? 'ಸರಿ!' : 'Correct!',
    partial: language === 'kn' ? 'ಭಾಗಶಃ ಸರಿ!' : 'Partially Correct!',
    wrong: language === 'kn' ? 'ತಪ್ಪು!' : 'Incorrect!',
    next: language === 'kn' ? 'ಮುಂದಿನ ಪ್ರಶ್ನೆ' : 'Next Question',
    submit: language === 'kn' ? 'ಉತ್ತರ ಸಲ್ಲಿಸಿ' : 'Submit Answer',
    selectMatch: language === 'kn' ? '-- ಆಯ್ಕೆ ಮಾಡಿ --' : '-- Select Match --'
  };

  return (
    <div style={{
      backgroundColor: 'rgba(255, 255, 255, 0.95)',
      borderRadius: '20px',
      boxShadow: 'var(--shadow-md)',
      color: 'var(--text-dark)',
      position: 'relative',
      maxWidth: '600px',
      margin: '0 auto',
      width: '100%',
      display: 'flex',
      flexDirection: 'column',
      /* Fill the parent flex container so sticky works */
      flex: 1,
      overflow: 'hidden',
      minHeight: 0,
    }}>
      {/* Scrollable content area */}
      <div style={{ overflowY: 'auto', flex: 1, padding: '20px', paddingBottom: '8px', WebkitOverflowScrolling: 'touch' }}>
      <h2 style={{ fontSize: '1.4rem', marginBottom: '20px', lineHeight: '1.4' }}>
        {questionData.question}
      </h2>

      {/* SINGLE CHOICE */}
      {qType === 'single' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {questionData.options.map((opt, idx) => {
            let btnBg = '#f0f0f0';
            let btnColor = 'var(--text-dark)';
            
            if (showReasoning) {
              if (String(opt).trim() === String(questionData.answer).trim()) {
                btnBg = '#06D6A0';
                btnColor = 'white';
              } else if (opt === selectedOption && String(opt).trim() !== String(questionData.answer).trim()) {
                btnBg = '#EF476F';
                btnColor = 'white';
              }
            } else if (opt === selectedOption) {
              btnBg = 'var(--tuk-yellow)';
            }

            return (
              <button
                key={idx}
                disabled={showReasoning}
                onClick={() => handleSingleSubmit(opt)}
                style={{
                  padding: '15px', borderRadius: '10px', border: '2px solid transparent',
                  backgroundColor: btnBg, color: btnColor, fontSize: '1.1rem',
                  fontWeight: '600', cursor: showReasoning ? 'default' : 'pointer',
                  textAlign: 'left', transition: 'all 0.2s', display: 'flex',
                  justifyContent: 'space-between', alignItems: 'center',
                  boxShadow: showReasoning ? 'none' : '0 4px 6px rgba(0,0,0,0.05)'
                }}
              >
                {opt}
                {showReasoning && String(opt).trim() === String(questionData.answer).trim() && <Check size={20} />}
                {showReasoning && opt === selectedOption && String(opt).trim() !== String(questionData.answer).trim() && <X size={20} />}
              </button>
            );
          })}
        </div>
      )}

      {/* MULTIPLE CHOICE */}
      {qType === 'multiple' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{ color: 'var(--accent-color)', fontSize: '0.9rem', marginBottom: '5px', fontWeight: 'bold' }}>
            <Lightbulb size={14} style={{ display: 'inline', marginRight: '5px', verticalAlign: 'text-bottom' }} />
            {language === 'kn' ? 'ಇದು ಬಹು-ಆಯ್ಕೆಯ ಪ್ರಶ್ನೆ (ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಸರಿ ಉತ್ತರಗಳಿರಬಹುದು)' : 'Multiple Choice Question (Select all that apply)'}
          </div>
          {questionData.options.map((opt, idx) => {
            const isSelected = selectedOptions.includes(opt);
            const isActuallyCorrect = (questionData.answer || []).includes(opt);
            
            let btnBg = '#f0f0f0';
            let btnColor = 'var(--text-dark)';
            let borderColor = 'transparent';

            if (showReasoning) {
              if (isActuallyCorrect) {
                btnBg = '#06D6A0';
                btnColor = 'white';
              } else if (isSelected && !isActuallyCorrect) {
                btnBg = '#EF476F';
                btnColor = 'white';
              }
            } else if (isSelected) {
              borderColor = 'var(--accent-color)';
              btnBg = '#e6f7ff';
            }

            return (
              <div
                key={idx}
                onClick={() => handleMultipleToggle(opt)}
                style={{
                  padding: '15px', borderRadius: '10px', border: `2px solid ${borderColor}`,
                  backgroundColor: btnBg, color: btnColor, fontSize: '1.1rem',
                  fontWeight: '600', cursor: showReasoning ? 'default' : 'pointer',
                  display: 'flex', alignItems: 'center', gap: '15px', transition: 'all 0.2s'
                }}
              >
                <div style={{
                  width: '24px', height: '24px', borderRadius: '4px', border: '2px solid',
                  borderColor: isSelected ? 'var(--accent-color)' : '#ccc',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  backgroundColor: isSelected ? 'var(--accent-color)' : 'white'
                }}>
                  {isSelected && <Check size={16} color="white" />}
                </div>
                <div style={{ flex: 1 }}>{opt}</div>
                {showReasoning && isActuallyCorrect && <Check size={20} />}
                {showReasoning && isSelected && !isActuallyCorrect && <X size={20} />}
              </div>
            );
          })}
          {!showReasoning && (
            <button className="btn btn-primary" onClick={handleMultipleSubmit} style={{ marginTop: '10px' }} disabled={selectedOptions.length === 0}>
              {labels.submit}
            </button>
          )}
        </div>
      )}

      {/* MATCHING */}
      {qType === 'match' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          {questionData.pairs.map((pair, idx) => {
            const userSelection = selectedMatches[pair.left] || '';
            const isCorrectMatch = userSelection === pair.right;
            let bgColor = '#f9f9f9';
            if (showReasoning) {
              bgColor = isCorrectMatch ? 'rgba(6, 214, 160, 0.2)' : 'rgba(239, 71, 111, 0.2)';
            }

            return (
              <div key={idx} style={{ 
                display: 'flex', gap: '10px', alignItems: 'center', 
                backgroundColor: bgColor, padding: '10px', borderRadius: '10px',
                flexDirection: window.innerWidth < 500 ? 'column' : 'row'
              }}>
                <div style={{ flex: 1, fontWeight: 'bold' }}>{pair.left}</div>
                <div style={{ flex: 1, width: '100%' }}>
                  <select 
                    disabled={showReasoning}
                    value={userSelection}
                    onChange={(e) => handleMatchChange(pair.left, e.target.value)}
                    style={{ 
                      width: '100%', padding: '10px', borderRadius: '8px', 
                      border: '1px solid #ccc', fontSize: '1rem' 
                    }}
                  >
                    <option value="" disabled>{labels.selectMatch}</option>
                    {shuffledRights.map((r, i) => (
                      <option key={i} value={r}>{r}</option>
                    ))}
                  </select>
                </div>
                {showReasoning && isCorrectMatch && <Check size={24} color="#06D6A0" />}
                {showReasoning && !isCorrectMatch && <X size={24} color="#EF476F" />}
              </div>
            );
          })}
          {!showReasoning && (
            <button 
              className="btn btn-primary" 
              onClick={handleMatchSubmit} 
              style={{ marginTop: '10px' }}
              disabled={Object.keys(selectedMatches).length !== questionData.pairs.length}
            >
              {labels.submit}
            </button>
          )}
        </div>
      )}

      {/* REASONING (scrollable, inside the scroll area) */}
      {showReasoning && (
        <div style={{
          marginTop: '20px', padding: '15px',
          backgroundColor: isCorrect ? 'rgba(6, 214, 160, 0.1)' : (isPartiallyCorrect ? 'rgba(255, 209, 102, 0.2)' : 'rgba(239, 71, 111, 0.1)'),
          borderRadius: '10px', borderLeft: `5px solid ${isCorrect ? '#06D6A0' : (isPartiallyCorrect ? '#FFD166' : '#EF476F')}`,
          animation: 'fadeIn 0.5s'
        }}>
          <h3 style={{ display: 'flex', alignItems: 'center', gap: '5px', color: isCorrect ? '#06D6A0' : (isPartiallyCorrect ? '#F4A261' : '#EF476F'), margin: '0 0 10px 0' }}>
            {isCorrect ? <Check size={20}/> : (isPartiallyCorrect ? <Check size={20}/> : <X size={20}/>)} 
            {isCorrect ? labels.correct : (isPartiallyCorrect ? labels.partial : labels.wrong)}
          </h3>
          <p style={{ margin: 0, fontSize: '0.95rem', lineHeight: '1.5' }}>
            <strong><Lightbulb size={16} style={{display: 'inline', verticalAlign: 'text-bottom'}}/> {labels.reasoning}:</strong> {questionData.reasoning}
          </p>
        </div>
      )}

      {/* Close scrollable area */}
      </div>

      {/* NEXT QUESTION — sticky footer, always visible above browser chrome */}
      {showReasoning && (
        <div style={{
          position: 'sticky',
          bottom: 0,
          backgroundColor: 'rgba(255, 255, 255, 0.98)',
          backdropFilter: 'blur(8px)',
          WebkitBackdropFilter: 'blur(8px)',
          padding: '12px 20px',
          paddingBottom: 'calc(12px + env(safe-area-inset-bottom, 0px))',
          borderTop: '1px solid rgba(0,0,0,0.07)',
          borderRadius: '0 0 20px 20px',
          zIndex: 10,
        }}>
          <button 
            className="btn btn-secondary" 
            onClick={handleNext}
            style={{
              width: '100%',
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              gap: '10px',
              fontSize: '1.05rem',
              padding: '14px',
            }}
          >
            {labels.next} <ArrowRight size={20} />
          </button>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
