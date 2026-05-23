import React, { useState, useEffect } from 'react';

const scienceQuestions = [
  { q: "What powers the sun?", a: "Nuclear Fusion", options: ["Magic", "Fire", "Nuclear Fusion", "Electricity"] },
  { q: "Water freezes into...", a: "Ice", options: ["Steam", "Ice", "Jelly", "Glass"] },
  { q: "Which planet is known as the Red Planet?", a: "Mars", options: ["Venus", "Mars", "Jupiter", "Saturn"] },
  { q: "What gas do plants 'breathe' in?", a: "Carbon Dioxide", options: ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"] },
  { q: "The force that pulls us to the ground is...", a: "Gravity", options: ["Magnetism", "Gravity", "Friction", "Wind"] }
];

const ScienceGame = ({ level, onCorrect, onWrong }) => {
  const [question, setQuestion] = useState(null);

  const loadQuestion = () => {
    // Pick a random question
    const q = scienceQuestions[Math.floor(Math.random() * scienceQuestions.length)];
    // Shuffle options
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
      animation: 'slideIn 0.4s ease-out'
    }}>
      <h3 style={{ color: 'var(--tuk-blue)', marginBottom: '10px' }}>Fuel the Reactor!</h3>
      <div style={{
        fontSize: '1.2rem',
        fontWeight: 'bold',
        color: '#06D6A0',
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
            style={{ fontSize: '1rem', padding: '10px' }}
          >
            {opt}
          </button>
        ))}
      </div>
    </div>
  );
};

export default ScienceGame;
