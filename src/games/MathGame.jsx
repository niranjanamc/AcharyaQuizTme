import React, { useState, useEffect } from 'react';

const MathGame = ({ level, onCorrect, onWrong }) => {
  const [problem, setProblem] = useState({ q: '', a: 0, options: [] });

  const generateProblem = () => {
    let num1, num2, op, ans;
    if (level < 3) {
      num1 = Math.floor(Math.random() * 10) + 1;
      num2 = Math.floor(Math.random() * 10) + 1;
      op = '+';
      ans = num1 + num2;
    } else if (level < 5) {
      num1 = Math.floor(Math.random() * 20) + 10;
      num2 = Math.floor(Math.random() * 10) + 1;
      op = '-';
      ans = num1 - num2;
    } else {
      num1 = Math.floor(Math.random() * 10) + 2;
      num2 = Math.floor(Math.random() * 10) + 2;
      op = 'x';
      ans = num1 * num2;
    }

    // Generate wrong options
    const options = new Set([ans]);
    while(options.size < 4) {
      const offset = Math.floor(Math.random() * 10) - 5;
      const wrongAns = ans + (offset === 0 ? 1 : offset);
      if (wrongAns > 0) options.add(wrongAns);
    }
    
    const shuffledOptions = Array.from(options).sort(() => Math.random() - 0.5);
    
    setProblem({ q: `${num1} ${op} ${num2} = ?`, a: ans, options: shuffledOptions });
  };

  useEffect(() => {
    generateProblem();
  }, [level]);

  const handleOptionClick = (opt) => {
    if (opt === problem.a) {
      onCorrect();
      generateProblem();
    } else {
      onWrong();
    }
  };

  return (
    <div style={{
      backgroundColor: 'white',
      padding: '20px',
      borderRadius: '20px',
      boxShadow: 'var(--shadow-md)',
      textAlign: 'center',
      animation: 'pulse 0.5s ease-out'
    }}>
      <h3 style={{ color: 'var(--tuk-blue)', marginBottom: '10px' }}>Fix the Engine Gear!</h3>
      <div style={{
        fontSize: '3rem',
        fontWeight: 'bold',
        color: 'var(--accent-color)',
        marginBottom: '20px',
        fontFamily: 'monospace'
      }}>
        {problem.q}
      </div>
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: '10px'
      }}>
        {problem.options.map((opt, i) => (
          <button 
            key={i} 
            className="btn btn-secondary"
            onClick={() => handleOptionClick(opt)}
            style={{ fontSize: '1.5rem', padding: '15px' }}
          >
            {opt}
          </button>
        ))}
      </div>
    </div>
  );
};

export default MathGame;
