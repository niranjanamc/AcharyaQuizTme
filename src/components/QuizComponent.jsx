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
  // Map image types to their effective answer type for logic reuse
  const effectiveType = qType.startsWith('image_') ? qType.replace('image_', '') : qType;

  useEffect(() => {
    setSelectedOption(null);
    setSelectedOptions([]);
    setSelectedMatches({});
    setShowReasoning(false);
    setIsCorrect(false);
    setIsPartiallyCorrect(false);

    if (effectiveType === 'match' && questionData.pairs) {
      const rights = questionData.pairs.map(p => p.right);
      setShuffledRights(rights.sort(() => Math.random() - 0.5));
    }
  }, [questionData, effectiveType]);

  if (!questionData) return <div>Loading...</div>;

  const handleSingleSubmit = (opt) => {
    soundEngine.playClick();
    const optId = typeof opt === 'object' ? opt.id : opt;
    setSelectedOption(optId);
    const correct = String(optId).trim() === String(questionData.answer).trim();
    setIsCorrect(correct);
    setShowReasoning(true);
  };

  const handleMultipleToggle = (opt) => {
    if (showReasoning) return;
    const optId = typeof opt === 'object' ? opt.id : opt;
    setSelectedOptions(prev => 
      prev.includes(optId) ? prev.filter(o => o !== optId) : [...prev, optId]
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
      padding: '20px',
      maxWidth: '600px',
      margin: '0 auto',
      width: '100%',
    }}>
      {/* IMAGE BLOCK — renders diagram/photo above question text */}
      {questionData.image && (
        <div style={{
          marginBottom: '16px',
          display: 'flex',
          justifyContent: 'center',
          backgroundColor: '#fafafa',
          borderRadius: '12px',
          padding: '16px',
          border: '1px solid #eee',
          overflow: 'hidden'
        }}>
          {questionData.image.type === 'svg' ? (
            <div 
              dangerouslySetInnerHTML={{ __html: questionData.image.svg }}
              style={{ maxWidth: '100%', maxHeight: '280px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
              role="img"
              aria-label={questionData.image.alt || ''}
            />
          ) : (
            <img 
              src={`/images/questions/${questionData.image.src}`}
              alt={questionData.image.alt || ''}
              style={{ maxWidth: '100%', maxHeight: '280px', objectFit: 'contain', borderRadius: '8px' }}
              loading="lazy"
            />
          )}
        </div>
      )}

      <h2 style={{ fontSize: '1.4rem', marginBottom: '20px', lineHeight: '1.4' }}>
        {questionData.question}
      </h2>

      {/* SINGLE CHOICE (also handles image_single) */}
      {effectiveType === 'single' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          {questionData.options.map((opt, idx) => {
            const optId = typeof opt === 'object' ? opt.id : opt;
            const optText = typeof opt === 'object' ? opt.text : opt;
            const optImage = typeof opt === 'object' ? opt.image : null;
            
            let btnBg = '#f0f0f0';
            let btnColor = 'var(--text-dark)';
            
            if (showReasoning) {
              if (String(optId).trim() === String(questionData.answer).trim()) {
                btnBg = '#06D6A0';
                btnColor = 'white';
              } else if (optId === selectedOption && String(optId).trim() !== String(questionData.answer).trim()) {
                btnBg = '#EF476F';
                btnColor = 'white';
              }
            } else if (optId === selectedOption) {
              btnBg = 'var(--accent-yellow)';
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
                  flexDirection: optImage ? 'column' : 'row',
                  justifyContent: optImage ? 'center' : 'space-between',
                  alignItems: 'center', gap: optImage ? '10px' : '0',
                  boxShadow: showReasoning ? 'none' : '0 4px 6px rgba(0,0,0,0.05)'
                }}
              >
                {optImage && (
                  <div style={{ width: '100%', display: 'flex', justifyContent: 'center', backgroundColor: 'white', padding: '10px', borderRadius: '8px' }}>
                    {optImage.type === 'svg' ? (
                      <div dangerouslySetInnerHTML={{ __html: optImage.svg }} style={{ maxWidth: '100%', maxHeight: '150px' }} />
                    ) : (
                      <img src={`/images/questions/${optImage.src}`} alt={optImage.alt || ''} style={{ maxWidth: '100%', maxHeight: '150px', objectFit: 'contain' }} loading="lazy" />
                    )}
                  </div>
                )}
                <div style={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span>{optText}</span>
                  <div>
                    {showReasoning && String(optId).trim() === String(questionData.answer).trim() && <Check size={20} />}
                    {showReasoning && optId === selectedOption && String(optId).trim() !== String(questionData.answer).trim() && <X size={20} />}
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      )}

      {/* MULTIPLE CHOICE (also handles image_multiple) */}
      {effectiveType === 'multiple' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
          <div style={{ color: 'var(--accent-color)', fontSize: '0.9rem', marginBottom: '5px', fontWeight: 'bold' }}>
            <Lightbulb size={14} style={{ display: 'inline', marginRight: '5px', verticalAlign: 'text-bottom' }} />
            {language === 'kn' ? 'ಇದು ಬಹು-ಆಯ್ಕೆಯ ಪ್ರಶ್ನೆ (ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಸರಿ ಉತ್ತರಗಳಿರಬಹುದು)' : 'Multiple Choice Question (Select all that apply)'}
          </div>
          {questionData.options.map((opt, idx) => {
            const optId = typeof opt === 'object' ? opt.id : opt;
            const optText = typeof opt === 'object' ? opt.text : opt;
            const optImage = typeof opt === 'object' ? opt.image : null;
            
            const isSelected = selectedOptions.includes(optId);
            const isActuallyCorrect = (questionData.answer || []).map(String).includes(String(optId));
            
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
                  display: 'flex', flexDirection: optImage ? 'column' : 'row',
                  alignItems: optImage ? 'flex-start' : 'center', gap: '15px', transition: 'all 0.2s'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', width: '100%', gap: '15px' }}>
                  <div style={{
                    width: '24px', height: '24px', borderRadius: '6px', flexShrink: 0,
                    border: `2px solid ${isSelected ? 'var(--accent-color)' : '#ccc'}`,
                    backgroundColor: isSelected ? 'var(--accent-color)' : 'white',
                    display: 'flex', justifyContent: 'center', alignItems: 'center'
                  }}>
                    {isSelected && <Check size={16} color="white" strokeWidth={3} />}
                  </div>
                  <div style={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <span>{optText}</span>
                    <div>
                      {showReasoning && isActuallyCorrect && <Check size={20} />}
                      {showReasoning && isSelected && !isActuallyCorrect && <X size={20} />}
                    </div>
                  </div>
                </div>
                
                {optImage && (
                  <div style={{ width: '100%', display: 'flex', justifyContent: 'center', backgroundColor: 'white', padding: '10px', borderRadius: '8px', marginTop: '5px' }}>
                    {optImage.type === 'svg' ? (
                      <div dangerouslySetInnerHTML={{ __html: optImage.svg }} style={{ maxWidth: '100%', maxHeight: '150px' }} />
                    ) : (
                      <img src={`/images/questions/${optImage.src}`} alt={optImage.alt || ''} style={{ maxWidth: '100%', maxHeight: '150px', objectFit: 'contain' }} loading="lazy" />
                    )}
                  </div>
                )}
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
      {effectiveType === 'match' && (
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

      {/* REASONING & NEXT QUESTION */}
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
          <p style={{ margin: '0 0 15px 0', fontSize: '0.95rem', lineHeight: '1.5' }}>
            <strong><Lightbulb size={16} style={{display: 'inline', verticalAlign: 'text-bottom'}}/> {labels.reasoning}:</strong> {questionData.reasoning}
          </p>
          <button 
            className="btn btn-secondary" 
            onClick={handleNext}
            style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '10px', fontSize: '1.05rem', padding: '14px' }}
          >
            {labels.next} <ArrowRight size={20} />
          </button>
        </div>
      )}
    </div>
  );
};

export default QuizComponent;
