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
  
  const [language, setLanguage] = useState('en');
  const [selectedChapters, setSelectedChapters] = useState([]);
  const [stats, setStats] = useState({ attempted: 0, correct: 0, wrong: 0 });

  const startGame = (config) => {
    setScore(0);
    setLevel(1);
    setLives(3);
    setStats({ attempted: 0, correct: 0, wrong: 0 });
    
    if (config) {
      setLanguage(config.language);
      setSelectedChapters(config.selectedChapters);
    }
    
    setGameState('playing');
  };

  const handleCorrect = () => {
    soundEngine.playCorrect();
    const newScore = score + 10 * level;
    setScore(newScore);
    setStats(s => ({ ...s, attempted: s.attempted + 1, correct: s.correct + 1 }));
  };

  const handleLevelUp = () => {
    soundEngine.playLevelUp();
    setLevel(l => l + 1);
  };

  const handleExhausted = () => {
    setGameState('completed');
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
            subject={selectedChapters.length > 1 ? 'mixed' : selectedChapters[0]?.subjectId} 
            onBuyLife={buyLifeFromHeader} 
            language={language}
          />
          <GameArea 
            level={level} 
            selectedChapters={selectedChapters}
            language={language}
            onCorrect={handleCorrect} 
            onWrong={handleWrong} 
            onLevelUp={handleLevelUp}
            onExhausted={handleExhausted}
          />
        </>
      )}

      {gameState === 'completed' && (
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', color: 'white', padding: '20px', textAlign: 'center' }}>
          <h1 style={{ fontSize: '3rem', color: '#06D6A0', marginBottom: '20px' }}>🏆</h1>
          <h2 style={{ fontSize: '2rem', marginBottom: '10px' }}>
            {language === 'kn' ? 'ಪಠ್ಯಕ್ರಮ ಪೂರ್ಣಗೊಂಡಿದೆ!' : 'Curriculum Completed!'}
          </h2>
          <p style={{ fontSize: '1.2rem', marginBottom: '30px', opacity: 0.9 }}>
            {language === 'kn' ? 'ನೀವು ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿದ್ದೀರಿ. ಅಭಿನಂದನೆಗಳು!' : 'You have answered all questions in the selected chapters. Congratulations!'}
          </p>
          <div style={{ background: 'rgba(255,255,255,0.1)', padding: '20px', borderRadius: '15px', marginBottom: '30px' }}>
            <p><strong>{language === 'kn' ? 'ಅಂತಿಮ ಸ್ಕೋರ್' : 'Final Score'}:</strong> {score}</p>
            <p><strong>{language === 'kn' ? 'ಸರಿಯಾದ ಉತ್ತರಗಳು' : 'Correct'}:</strong> {stats.correct} / {stats.attempted}</p>
          </div>
          <button className="btn btn-primary" onClick={() => startGame()}>
            {language === 'kn' ? 'ಮತ್ತೆ ಆಡಿ' : 'Play Again'}
          </button>
        </div>
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
