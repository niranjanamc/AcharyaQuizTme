import React, { useState } from 'react';
import { Play, Settings, BookOpen } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';

const SUBJECTS = [
  { id: 'maths', label: 'Maths / ಗಣಿತ' },
  { id: 'science', label: 'Science / ವಿಜ್ಞಾನ' },
  { id: 'kannada', label: 'Kannada / ಕನ್ನಡ' },
  { id: 'history', label: 'History / ಇತಿಹಾಸ' },
  { id: 'gk', label: 'GK / ಸಾಮಾನ್ಯ ಜ್ಞಾನ' },
  { id: 'english', label: 'English / ಇಂಗ್ಲಿಷ್' },
  { id: 'puzzles', label: 'Puzzles / ಒಗಟುಗಳು' },
  { id: 'spellbee', label: 'Spell Bee / ಕಾಗುಣಿತ' }
];

const MainMenu = ({ onStart }) => {
  const [selectedSubjects, setSelectedSubjects] = useState(['maths', 'science', 'kannada', 'history']);
  const [language, setLanguage] = useState('en');

  const toggleSubject = (id) => {
    soundEngine.playClick();
    setSelectedSubjects(prev => 
      prev.includes(id) ? prev.filter(s => s !== id) : [...prev, id]
    );
  };

  const handleStart = () => {
    soundEngine.playClick();
    if (selectedSubjects.length === 0) {
      alert("Please select at least one subject!");
      return;
    }
    onStart({ subjects: selectedSubjects, language });
  };

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100%',
      padding: '20px',
      textAlign: 'center',
      color: 'white',
      overflowY: 'auto'
    }}>
      <div style={{ animation: 'bounce 2s infinite ease-in-out', marginBottom: '1rem' }}>
        <h1 style={{ 
          fontSize: '2.5rem', 
          textShadow: '2px 4px 0px rgba(0,0,0,0.2)',
          margin: 0
        }}>
          Acharya
        </h1>
        <h2 style={{
          fontSize: '3.5rem',
          color: 'var(--accent-color)',
          textShadow: '3px 6px 0px rgba(0,0,0,0.2)',
          margin: '-10px 0 0 0'
        }}>
          QUIZ TIME
        </h2>
      </div>

      <div style={{
        backgroundColor: 'rgba(38, 70, 83, 0.6)',
        padding: '20px',
        borderRadius: '15px',
        marginBottom: '1rem',
        backdropFilter: 'blur(5px)',
        width: '100%',
        maxWidth: '400px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
          <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '5px' }}>
            <Settings size={20}/> Language / ಭಾಷೆ
          </h3>
          <div style={{ display: 'flex', gap: '10px' }}>
            <button 
              className={`btn ${language === 'en' ? 'btn-secondary' : 'btn-disabled'}`}
              onClick={() => { soundEngine.playClick(); setLanguage('en'); }}
              style={{ padding: '5px 15px', fontSize: '1rem' }}
            >
              ENG
            </button>
            <button 
              className={`btn ${language === 'kn' ? 'btn-secondary' : 'btn-disabled'}`}
              onClick={() => { soundEngine.playClick(); setLanguage('kn'); }}
              style={{ padding: '5px 15px', fontSize: '1rem' }}
            >
              ಕನ್ನಡ
            </button>
          </div>
        </div>

        <h3 style={{ margin: '0 0 10px 0', textAlign: 'left', display: 'flex', alignItems: 'center', gap: '5px' }}>
          <BookOpen size={20}/> Choose Subjects
        </h3>
        <div style={{
          display: 'grid',
          gridTemplateColumns: '1fr 1fr',
          gap: '10px',
          textAlign: 'left'
        }}>
          {SUBJECTS.map(sub => (
            <label key={sub.id} style={{ display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer' }}>
              <input 
                type="checkbox" 
                checked={selectedSubjects.includes(sub.id)}
                onChange={() => toggleSubject(sub.id)}
                style={{ width: '18px', height: '18px' }}
              />
              <span style={{ fontSize: '0.9rem' }}>{sub.label}</span>
            </label>
          ))}
        </div>
      </div>

      <button 
        className="btn btn-primary" 
        onClick={handleStart}
        style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '1.5rem', width: '100%', maxWidth: '400px', justifyContent: 'center' }}
      >
        <Play size={24} fill="currentColor" /> START QUIZ
      </button>
    </div>
  );
};

export default MainMenu;
