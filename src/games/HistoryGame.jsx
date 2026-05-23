import React, { useState, useEffect } from 'react';

const historyQuestions = [
  { q: "Which monument is famous for its white marble and is located in Agra?", a: "Taj Mahal", options: ["Red Fort", "Taj Mahal", "Qutub Minar", "Charminar"] },
  { q: "Who was the first Prime Minister of independent India?", a: "Jawaharlal Nehru", options: ["Mahatma Gandhi", "Sardar Patel", "Jawaharlal Nehru", "B.R. Ambedkar"] },
  { q: "Which empire was ruled by Krishnadevaraya?", a: "Vijayanagara", options: ["Maurya", "Mughal", "Vijayanagara", "Gupta"] },
  { q: "What did early humans use to make tools?", a: "Stone", options: ["Plastic", "Steel", "Stone", "Glass"] },
  { q: "The Indus Valley Civilization is also known as the...", a: "Harappan Civilization", options: ["Vedic Age", "Harappan Civilization", "Chola Dynasty", "Aryan Age"] }
];

const HistoryGame = ({ level, onCorrect, onWrong }) => {
  const [question, setQuestion] = useState(null);

  const loadQuestion = () => {
    const q = historyQuestions[Math.floor(Math.random() * historyQuestions.length)];
    const shuffled = [...q.options].sort(() => Math.random() - 0.5);
    setQuestion({ ...q, options: shuffled });
  };

  useEffect(() => {
    loadQuestion();
  }, [level]);

  const handleOptionClick = (opt) => {
    if (opt === question.a) {
      onCorrect();
      loadQuestion();
    } else {
      onWrong();
    }
  };

  if (!question) return null;

  return (
    <div style={{
      backgroundColor: 'white',
      padding: '20px',
      borderRadius: '20px',
      boxShadow: 'var(--shadow-md)',
      textAlign: 'center',
      animation: 'pulse 0.4s ease-out'
    }}>
      <h3 style={{ color: 'var(--tuk-blue)', marginBottom: '10px' }}>Convince the Locals!</h3>
      <p style={{ fontSize: '0.9rem', opacity: 0.7, marginBottom: '10px' }}>Answer their question to get a Tuk-Tuk part.</p>
      <div style={{
        fontSize: '1.2rem',
        fontWeight: 'bold',
        color: '#FFB703',
        marginBottom: '20px',
      }}>
        {question.q}
      </div>
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: '10px'
      }}>
        {question.options.map((opt, i) => (
          <button 
            key={i} 
            className="btn btn-primary"
            onClick={() => handleOptionClick(opt)}
            style={{ fontSize: '1rem', padding: '10px', backgroundColor: '#FFD166' }}
          >
            {opt}
          </button>
        ))}
      </div>
    </div>
  );
};

export default HistoryGame;
