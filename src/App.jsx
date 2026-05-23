import React, { useState } from 'react';
import MainMenu from './components/MainMenu';
import GameArea from './components/GameArea';
import Header from './components/Header';
import GameOver from './components/GameOver';
import { soundEngine } from './utils/AudioEngine';

function App() {
  const [gameState, setGameState] = useState('menu'); // 'menu', 'playing', 'buylife', 'gameover'
  const [score, setScore] = useState(0);
  const [level, setLevel] = useState(1);
  const [lives, setLives] = useState(3);
  
  // New State
  const [language, setLanguage] = useState('en');
  const [classId, setClassId] = useState('');
  const [subjectId, setSubjectId] = useState('');
  const [chapterId, setChapterId] = useState('');
  const [stats, setStats] = useState({ attempted: 0, correct: 0, wrong: 0 });

  const startGame = (config) => {
    setScore(0);
    setLevel(1);
    setLives(3);
    setStats({ attempted: 0, correct: 0, wrong: 0 });
    
    if (config) {
      setLanguage(config.language);
      setClassId(config.classId);
      setSubjectId(config.subjectId);
      setChapterId(config.chapterId);
    }
    
    setGameState('playing');
  };

  const handleCorrect = () => {
    soundEngine.playCorrect();
    const newScore = score + 10 * level;
    setScore(newScore);
    setStats(s => ({ ...s, attempted: s.attempted + 1, correct: s.correct + 1 }));
    
    // Level up every 50 points
    if (Math.floor(newScore / 50) > Math.floor(score / 50)) {
      soundEngine.playLevelUp();
      setLevel(level + 1);
    }
  };

  const handleWrong = () => {
    soundEngine.playIncorrect();
    setStats(s => ({ ...s, attempted: s.attempted + 1, wrong: s.wrong + 1 }));
    setLives(l => {
      const newLives = l - 1;
      if (newLives <= 0) {
        if (score >= 50) {
          setGameState('buylife');
        } else {
          setGameState('gameover');
        }
        return 0;
      }
      return newLives;
    });
  };

  const buyLifeFromHeader = () => {
    soundEngine.playClick();
    if (score >= 50 && lives < 3) {
      setScore(s => s - 50);
      setLives(l => l + 1);
    }
  };

  const buyLifeFromModal = (buy) => {
    soundEngine.playClick();
    if (buy && score >= 50) {
      setScore(s => s - 50);
      setLives(1);
      setGameState('playing');
    } else {
      setGameState('gameover');
    }
  };

  return (
    <div style={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column' }}>
      {gameState === 'menu' && <MainMenu onStart={startGame} />}
      
      {(gameState === 'playing' || gameState === 'buylife') && (
        <>
          <Header 
            score={score} 
            level={level} 
            lives={lives} 
            subject={`${subjectId}`} 
            onBuyLife={buyLifeFromHeader} 
            language={language}
          />
          <GameArea 
            level={level} 
            classId={classId}
            subjectId={subjectId}
            chapterId={chapterId}
            language={language}
            onCorrect={handleCorrect} 
            onWrong={handleWrong} 
          />
        </>
      )}

      {gameState === 'buylife' && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h2 style={{ color: 'var(--accent-color)', marginBottom: '10px' }}>
              {language === 'kn' ? 'ವಿಮಾನ ಕೆಟ್ಟುಹೋಯಿತು!' : 'Vimana Crashed!'}
            </h2>
            <p style={{ marginBottom: '20px' }}>
              {language === 'kn' ? '50 ಅಂಕಗಳನ್ನು ನೀಡಿ 1 ಜೀವ ಪಡೆಯುವಿರಾ?' : 'Spend 50 score to buy 1 extra life?'}
            </p>
            <div style={{ display: 'flex', gap: '10px', justifyContent: 'center' }}>
              <button className="btn btn-secondary" onClick={() => buyLifeFromModal(true)}>
                {language === 'kn' ? 'ಹೌದು (Yes)' : 'YES (-50 Pts)'}
              </button>
              <button className="btn" style={{ backgroundColor: '#ccc', color: '#333' }} onClick={() => buyLifeFromModal(false)}>
                {language === 'kn' ? 'ಇಲ್ಲ (No)' : 'NO (Give Up)'}
              </button>
            </div>
          </div>
        </div>
      )}

      {gameState === 'gameover' && (
        <GameOver 
          score={score} 
          level={level} 
          stats={stats}
          language={language}
          onRestart={() => startGame()} 
        />
      )}
    </div>
  );
}

export default App;
