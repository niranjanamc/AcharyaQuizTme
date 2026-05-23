import React, { useState } from 'react';
import { Play, Settings, BookOpen } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';
import catalog from '../data/catalog.json';

const MainMenu = ({ onStart }) => {
  const [language, setLanguage] = useState('en');

  // Cascading selections
  const [selectedClass, setSelectedClass] = useState(catalog.classes[0].id);
  const classObj = catalog.classes.find(c => c.id === selectedClass);
  
  const [selectedSubject, setSelectedSubject] = useState(classObj.subjects[0].id);
  const subjectObj = classObj.subjects.find(s => s.id === selectedSubject) || classObj.subjects[0];
  
  const [selectedChapter, setSelectedChapter] = useState(subjectObj.chapters[0].id);

  const handleClassChange = (e) => {
    soundEngine.playClick();
    const newClass = e.target.value;
    setSelectedClass(newClass);
    const newClassObj = catalog.classes.find(c => c.id === newClass);
    const newSubj = newClassObj.subjects[0].id;
    setSelectedSubject(newSubj);
    setSelectedChapter(newClassObj.subjects[0].chapters[0].id);
  };

  const handleSubjectChange = (e) => {
    soundEngine.playClick();
    const newSubj = e.target.value;
    setSelectedSubject(newSubj);
    const newSubjObj = classObj.subjects.find(s => s.id === newSubj);
    setSelectedChapter(newSubjObj.chapters[0].id);
  };

  const handleChapterChange = (e) => {
    soundEngine.playClick();
    setSelectedChapter(e.target.value);
  };

  const handleStart = () => {
    soundEngine.playClick();
    onStart({ 
      language, 
      classId: selectedClass, 
      subjectId: selectedSubject, 
      chapterId: selectedChapter 
    });
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
          <BookOpen size={20}/> Curriculum
        </h3>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', textAlign: 'left' }}>
          <label style={{ display: 'flex', flexDirection: 'column', fontSize: '0.9rem' }}>
            Class / Category:
            <select value={selectedClass} onChange={handleClassChange} style={{ padding: '8px', borderRadius: '5px', marginTop: '5px' }}>
              {catalog.classes.map(c => <option key={c.id} value={c.id}>{c.name}</option>)}
            </select>
          </label>
          
          <label style={{ display: 'flex', flexDirection: 'column', fontSize: '0.9rem' }}>
            Subject:
            <select value={selectedSubject} onChange={handleSubjectChange} style={{ padding: '8px', borderRadius: '5px', marginTop: '5px' }}>
              {classObj.subjects.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
            </select>
          </label>

          <label style={{ display: 'flex', flexDirection: 'column', fontSize: '0.9rem' }}>
            Chapter:
            <select value={selectedChapter} onChange={handleChapterChange} style={{ padding: '8px', borderRadius: '5px', marginTop: '5px' }}>
              {subjectObj.chapters.map(ch => <option key={ch.id} value={ch.id}>{ch.name}</option>)}
            </select>
          </label>
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
