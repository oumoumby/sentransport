import './StatReseau.css';

function StatReseau({ lignes }) {
  const nombreLignes = lignes.length;
  const nombreArretsTotal = lignes.reduce((somme, ligne) => somme + ligne.arrets, 0);
  const lignePlusArrets = lignes.reduce((max, ligne) => 
    ligne.arrets > max.arrets ? ligne : max
  );

  return (
    <div className="stat-reseau">
      <div className="stat-item">
        <h3>{nombreLignes}</h3>
        <p>Lignes disponibles</p>
      </div>
      <div className="stat-item">
        <h3>{nombreArretsTotal}</h3>
        <p>Arrêts au total</p>
      </div>
      <div className="stat-item">
        <h3>Ligne {lignePlusArrets.numero}</h3>
        <p>Plus d'arrêts ({lignePlusArrets.arrets})</p>
      </div>
    </div>
  );
}

export default StatReseau;
