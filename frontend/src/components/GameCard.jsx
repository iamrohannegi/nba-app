import styles from './GameCard.module.css';

const GameCard = (props) => {
    return (
        <div className={styles.gamecard}>
            <h3 className={styles.gamecard__name}>{props.name}</h3>
            <section className={styles.gamecard__ratings}>
              <h4 className={styles.gamecard__sectionheading}>Ratings</h4>
              <ul>
                { Object.entries(props.ratings).map(([ratingName, rating]) => {
                  return (
                      <li key={`${props.id}/${ratingName}`}>
                        <span className={styles.gamecard__ratingname}>{ratingName}</span>
                        <span className={styles.gamecard__rating}>{rating}</span>
                      </li>
                )})}
              </ul>
            </section>
            <section className={styles.gamecard__score}>
              <h4 className={styles.gamecard__sectionheading}>Scores</h4>
              <div>
                <h4 className={styles.gamecard__teamdata}>{props.teams.winner.team}({props.teams.winner.record})</h4>
                <span className={styles.gamecard__teamscore}>{props.teams.winner.score}</span>
              </div>
              <div>
                <h4 className={styles.gamecard__teamdata}>{props.teams.loser.team}({props.teams.loser.record})</h4>
                <span className={styles.gamecard__teamscore}>{props.teams.loser.score}</span>
              </div>
            </section>
            
        </div>
    );
};

export default GameCard