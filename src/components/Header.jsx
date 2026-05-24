import React, { useEffect, useState } from 'react';
import { Heart, Star, BookOpen, PlusCircle } from 'lucide-react';

const Header = ({ score, level, lives, subject, onBuyLife, language }) => {
  const [levelUpAnim, setLevelUpAnim] = useState(false);

  // Trigger animation when level changes
  useEffect(() => {
    if (level > 1) {
      setLevelUpAnim(true);
      setTimeout(() => setLevelUpAnim(false), 2000);
    }
  }, [level]);

  // Calculate progress to next level (every 50 points = next level)
  // Example: Score 0 -> level 1. Score 50 -> level 2.
  // Progress in current level = score % 50
  const progressPercent = Math.min(((score % 50) / 50) * 100, 100);

  const subjectNames = {
    maths: language === 'kn' ? 'ಗಣಿತ' : 'Maths',
    science: language === 'kn' ? 'ವಿಜ್ಞಾನ' : 'Science',
    kannada: language === 'kn' ? 'ಕನ್ನಡ' : 'Kannada',
    history: language === 'kn' ? 'ಇತಿಹಾಸ' : 'History',
    gk: language === 'kn' ? 'ಸಾ. ಜ್ಞಾನ' : 'GK',
    english: language === 'kn' ? 'ಇಂಗ್ಲಿಷ್' : 'English',
    puzzles: language === 'kn' ? 'ಒಗಟುಗಳು' : 'Puzzles',
    spellbee: language === 'kn' ? 'ಕಾಗುಣಿತ' : 'Spell Bee',
    mixed: language === 'kn' ? 'ಮಿಶ್ರ ಪಠ್ಯಕ್ರಮ' : 'Mixed Curriculum'
  };

  return (
    <div style={{
      padding: '15px 20px',
      backgroundColor: 'var(--text-dark)',
      borderBottomLeftRadius: '20px',
      borderBottomRightRadius: '20px',
      zIndex: 10,
      position: 'relative',
      color: 'white',
      boxShadow: 'var(--shadow-md)'
    }}>
      {levelUpAnim && (
        <div style={{
          position: 'absolute',
          top: '50px',
          left: '50%',
          transform: 'translateX(-50%)',
          fontSize: '3rem',
          fontWeight: 'bold',
          color: 'var(--tuk-yellow)',
          textShadow: '0 0 20px #FF9E00',
          animation: 'grandLevelUp 2s ease-out forwards',
          zIndex: 100,
          pointerEvents: 'none'
        }}>
          LEVEL UP!
        </div>
      )}

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
          <div style={{ 
            display: 'flex', 
            alignItems: 'center', 
            gap: '5px',
            fontWeight: 'bold',
            fontSize: '1.2rem',
            color: 'var(--tuk-yellow)'
          }}>
            <Star fill="currentColor" size={24} /> {score}
          </div>
          <div style={{
            backgroundColor: 'var(--secondary-bg)',
            padding: '4px 12px',
            borderRadius: '20px',
            color: 'white',
            fontWeight: 'bold',
            textTransform: 'uppercase',
            fontSize: '0.9rem',
            display: 'flex',
            alignItems: 'center',
            gap: '5px'
          }}>
            <BookOpen size={16} /> {subjectNames[subject] || subject} (Lvl {level})
          </div>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
          <div style={{ display: 'flex', gap: '2px' }}>
            {[...Array(3)].map((_, i) => (
              <Heart 
                key={i} 
                fill={i < lives ? "var(--accent-color)" : "transparent"} 
                color="var(--accent-color)"
                size={24}
                style={{ transition: 'all 0.3s' }}
              />
            ))}
          </div>
          {lives < 3 && score >= 50 && (
            <button 
              onClick={onBuyLife}
              style={{
                background: 'var(--secondary-bg)',
                border: 'none',
                borderRadius: '50px',
                padding: '5px 10px',
                color: 'white',
                fontWeight: 'bold',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '5px',
                fontSize: '0.8rem',
                boxShadow: 'var(--shadow-sm)'
              }}
            >
              <PlusCircle size={14} /> 50
            </button>
          )}
        </div>
      </div>

      <div className="progress-container">
        <div className="progress-fill" style={{ width: `${progressPercent}%` }}></div>
      </div>
    </div>
  );
};

export default Header;
