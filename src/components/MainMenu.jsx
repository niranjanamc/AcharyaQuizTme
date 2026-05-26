import React, { useState } from 'react';
import { Play, Settings, BookOpen, ChevronDown, ChevronRight, CheckSquare, Square } from 'lucide-react';
import { soundEngine } from '../utils/AudioEngine';
import catalog from '../data/catalog.json';
import menuTranslations from '../data/menuTranslations.json';

// Handles both plain-string ("ಗಣಿತ") and object ({en:"Math", kn:"ಗಣಿತ"}) formats
const getLabel = (key, language, fallback) => {
  const val = menuTranslations[key];
  if (!val) return fallback;
  if (typeof val === 'string') return language === 'kn' ? val : fallback;
  if (typeof val === 'object') return language === 'kn' ? (val.kn || fallback) : (val.en || fallback);
  return fallback;
};

const Checkbox = ({ checked, indeterminate, onClick }) => {
  if (checked) return <CheckSquare size={18} fill="var(--accent-color)" stroke="white" onClick={onClick} style={{ cursor: 'pointer' }} />;
  if (indeterminate) return <CheckSquare size={18} fill="#ccc" stroke="#333" onClick={onClick} style={{ cursor: 'pointer', opacity: 0.7 }} />;
  return <Square size={18} onClick={onClick} style={{ cursor: 'pointer' }} />;
};

const MainMenu = ({ onStart }) => {
  const [language, setLanguage] = useState('en');
  // Store selected chapters as strings: "classId/subjectId/chapterId"
  const [selected, setSelected] = useState(new Set());
  const [expanded, setExpanded] = useState(new Set([catalog.classes[0].id]));

  const toggleExpand = (id) => {
    soundEngine.playClick();
    const newExp = new Set(expanded);
    if (newExp.has(id)) newExp.delete(id);
    else newExp.add(id);
    setExpanded(newExp);
  };

  const toggleNode = (nodePaths, forceState) => {
    soundEngine.playClick();
    const newSel = new Set(selected);
    nodePaths.forEach(path => {
      if (forceState) newSel.add(path);
      else newSel.delete(path);
    });
    setSelected(newSel);
  };

  const getSelectionState = (nodePaths) => {
    let checkedCount = 0;
    nodePaths.forEach(p => {
      if (selected.has(p)) checkedCount++;
    });
    if (checkedCount === 0) return { checked: false, indeterminate: false };
    if (checkedCount === nodePaths.length) return { checked: true, indeterminate: false };
    return { checked: false, indeterminate: true };
  };

  const handleStart = () => {
    soundEngine.playClick();
    if (selected.size === 0) {
      alert(language === 'kn' ? "ದಯವಿಟ್ಟು ಕನಿಷ್ಠ ಒಂದು ಅಧ್ಯಾಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ!" : "Please select at least one chapter!");
      return;
    }
    
    // Parse selected paths back into objects
    const selectedChapters = Array.from(selected).map(path => {
      const [classId, subjectId, chapterId] = path.split('/');
      return { classId, subjectId, chapterId };
    });

    onStart({ language, selectedChapters });
  };

  return (
    <div style={{
      display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
      height: '100%', padding: '20px', color: 'var(--text-dark)', overflowY: 'auto'
    }}>
      <div style={{ animation: 'bounce 2s infinite ease-in-out', marginBottom: '1rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2.8rem', textShadow: '2px 4px 0px rgba(13, 71, 161, 0.1)', color: 'var(--text-dark)', margin: 0, fontWeight: '700' }}>
          {language === 'kn' ? 'ಭಗೀರಥ' : 'Bhagiratha'}
        </h1>
        <h2 style={{ fontSize: '3.5rem', color: 'var(--accent-color)', textShadow: '3px 6px 0px rgba(13, 71, 161, 0.15)', margin: '-10px 0 0 0', fontWeight: '700' }}>
          {language === 'kn' ? 'ರಸಪ್ರಶ್ನೆ' : 'QUIZ'}
        </h2>
      </div>

      <div style={{
        backgroundColor: 'rgba(255, 255, 255, 0.95)', 
        padding: '25px', 
        borderRadius: '20px',
        marginBottom: '1.2rem', 
        boxShadow: 'var(--shadow-md)', 
        color: 'var(--text-dark)',
        width: '100%', 
        maxWidth: '500px',
        backdropFilter: 'blur(10px)'
      }}>
        {/* Language Selection */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
          <h3 style={{ margin: 0, display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--text-dark)', fontSize: '1.1rem' }}>
            <Settings size={20}/> Language / ಭಾಷೆ
          </h3>
          <div style={{ display: 'flex', gap: '10px' }}>
            <button className={`btn ${language === 'en' ? 'btn-secondary' : 'btn-disabled'}`}
              onClick={() => { soundEngine.playClick(); setLanguage('en'); }}
              style={{ padding: '5px 15px', fontSize: '1rem' }}>ENG</button>
            <button className={`btn ${language === 'kn' ? 'btn-secondary' : 'btn-disabled'}`}
              onClick={() => { soundEngine.playClick(); setLanguage('kn'); }}
              style={{ padding: '5px 15px', fontSize: '1rem' }}>ಕನ್ನಡ</button>
          </div>
        </div>

        {/* Curriculum Tree */}
        <h3 style={{ margin: '0 0 10px 0', textAlign: 'left', display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--text-dark)', fontSize: '1.1rem' }}>
          <BookOpen size={20}/> {language === 'kn' ? 'ಪಠ್ಯಕ್ರಮದ ಆಯ್ಕೆ' : 'Curriculum Selection'}
        </h3>
        
        <div style={{ 
          display: 'flex', flexDirection: 'column', gap: '5px', textAlign: 'left', 
          maxHeight: '300px', overflowY: 'auto', 
          backgroundColor: 'rgba(13, 71, 161, 0.05)', 
          border: '1px solid rgba(13, 71, 161, 0.1)',
          padding: '12px', borderRadius: '12px' 
        }}>
          {catalog.classes.map(cls => {
            const classPaths = [];
            cls.subjects.forEach(sub => sub.chapters.forEach(ch => classPaths.push(`${cls.id}/${sub.id}/${ch.id}`)));
            const clsState = getSelectionState(classPaths);

            return (
              <div key={cls.id} style={{ marginBottom: '5px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span onClick={() => toggleExpand(cls.id)} style={{ cursor: 'pointer', display: 'flex', alignItems: 'center' }}>
                    {expanded.has(cls.id) ? <ChevronDown size={18} /> : <ChevronRight size={18} />}
                  </span>
                  <Checkbox 
                    checked={clsState.checked} indeterminate={clsState.indeterminate} 
                    onClick={() => toggleNode(classPaths, !clsState.checked)} 
                  />
                  <strong style={{ fontSize: '1.1rem', color: 'var(--text-dark)' }}>
                    {getLabel(cls.id, language, cls.name)}
                  </strong>
                </div>

                {expanded.has(cls.id) && (
                  <div style={{ paddingLeft: '25px', marginTop: '5px', display: 'flex', flexDirection: 'column', gap: '5px' }}>
                    {cls.subjects.map(sub => {
                      const subPaths = sub.chapters.map(ch => `${cls.id}/${sub.id}/${ch.id}`);
                      const subState = getSelectionState(subPaths);

                      return (
                        <div key={sub.id}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                            <span onClick={() => toggleExpand(sub.id)} style={{ cursor: 'pointer', display: 'flex', alignItems: 'center' }}>
                              {expanded.has(sub.id) ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
                            </span>
                            <Checkbox 
                              checked={subState.checked} indeterminate={subState.indeterminate} 
                              onClick={() => toggleNode(subPaths, !subState.checked)} 
                            />
                            <span style={{ fontWeight: '600', color: 'var(--text-dark)' }}>
                              {getLabel(`${cls.id}/${sub.id}`, language, sub.name)}
                            </span>
                          </div>

                          {expanded.has(sub.id) && (
                            <div style={{ paddingLeft: '25px', marginTop: '5px', display: 'flex', flexDirection: 'column', gap: '4px' }}>
                              {sub.chapters.map(ch => {
                                const chPath = `${cls.id}/${sub.id}/${ch.id}`;
                                const chChecked = selected.has(chPath);
                                return (
                                  <div key={ch.id} style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                                    <Checkbox 
                                      checked={chChecked} 
                                      onClick={() => toggleNode([chPath], !chChecked)} 
                                    />
                                    <span style={{ fontSize: '0.95rem', color: 'rgba(13, 71, 161, 0.8)', fontWeight: '500' }}>
                                      {getLabel(ch.id, language, ch.name)}
                                    </span>
                                  </div>
                                );
                              })}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <button className="btn btn-primary" onClick={handleStart}
        style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '1.4rem', width: '100%', maxWidth: '400px', justifyContent: 'center' }}>
        <Play size={24} fill="currentColor" /> {language === 'kn' ? `ರಸಪ್ರಶ್ನೆ ಪ್ರಾರಂಭಿಸಿ (${selected.size} ಅಧ್ಯಾಯಗಳು)` : `START QUIZ (${selected.size} chapters)`}
      </button>
    </div>
  );
};

export default MainMenu;
