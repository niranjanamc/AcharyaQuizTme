import React, { useState, useEffect } from 'react';

const kannadaWords = [
  { k: "ಶಾಲೆ (Shaale)", e: "School", options: ["House", "School", "Market", "Park"] },
  { k: "ಮನೆ (Mane)", e: "House", options: ["Tree", "Car", "House", "Book"] },
  { k: "ನಾಯಿ (Naayi)", e: "Dog", options: ["Cat", "Cow", "Dog", "Bird"] },
  { k: "ನೀರು (Neeru)", e: "Water", options: ["Milk", "Juice", "Fire", "Water"] },
  { k: "ಪುಸ್ತಕ (Pustaka)", e: "Book", options: ["Pen", "Bag", "Book", "Chair"] }
];

const KannadaGame = ({ level, onCorrect, onWrong }) => {
  const [question, setQuestion] = useState(null);

  const loadQuestion = () => {
    const q = kannadaWords[Math.floor(Math.random() * kannadaWords.length)];
    const shuffled = [...q.options].sort(() => Math.random() - 0.5);
    setQuestion({ ...q, options: shuffled });
  };

  useEffect(() => {
    loadQuestion();
  }, [level]);

  const handleOptionClick = (opt) => {
    if (opt === question.e) {
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
      animation: 'slideIn 0.4s ease-out'
    }}>
      <h3 style={{ color: 'var(--tuk-blue)', marginBottom: '10px' }}>Translate the Alien Script!</h3>
      <p style={{ fontSize: '0.9rem', opacity: 0.7, marginBottom: '10px' }}>(It looks suspiciously like Kannada...)</p>
      <div style={{
        fontSize: '2rem',
        fontWeight: 'bold',
        color: '#118AB2',
        marginBottom: '20px',
      }}>
        {question.k}
      </div>
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: '10px'
      }}>
        {question.options.map((opt, i) => (
          <button 
            key={i} 
            className="btn btn-secondary"
            onClick={() => handleOptionClick(opt)}
            style={{ fontSize: '1rem', padding: '10px', backgroundColor: '#118AB2' }}
          >
            {opt}
          </button>
        ))}
      </div>
    </div>
  );
};

export default KannadaGame;
