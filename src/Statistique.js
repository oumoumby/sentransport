import './Statistique.css';

function Statistique({ligne, arret}) {
  return (
    <div className="statistique-card">
      <div className="statistique-chiffre"> <p>{ligne} lignes</p></div>
      <div className="statistique-libelle"><p> {arret}</p> arrets</div>
    </div>
  );
}

export default Statistique;
