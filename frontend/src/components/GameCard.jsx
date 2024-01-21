import styles from './GameCard.module.css';

const GameCard = (props) => {
    return (
        <div className={styles.gamecard}>
            <h3 className={styles.gamecard__name}>{props.name}</h3>
            <div className={styles.gamecard__ratings}>
              <h4 className={styles.gamecard__heading}>Ratings</h4>
              <ul>
                { Object.entries(props.ratings).map(([ratingName, rating]) => {
                  return (
                      <li key={`${props.id}/${ratingName}`}>
                        <span className={styles.gamecard__ratingname}>{ratingName.split('_').join(' ')}</span>
                        <span className={styles.gamecard__rating}>{rating}</span>
                      </li>
                )})}
              </ul>
            </div>
            <div className={styles.gamecard__score}>
              <h4 className={styles.gamecard__heading}>Scores</h4>
              <div>
                <h4 className={styles.gamecard__teamdata}>
                  <span className={styles.gamecard__teamname}>{props.teams.winner.team}</span>
                  <span className={styles.gamecard__teamrecord}>({props.teams.winner.record})</span>
                </h4>
                <span className={styles.gamecard__teamscore}>{props.teams.winner.score}</span>
              </div>
              <div>
                <h4 className={styles.gamecard__teamdata}>
                    <span className={styles.gamecard__teamname}>{props.teams.loser.team}</span>
                    <span className={styles.gamecard__teamrecord}>({props.teams.loser.record})</span>
                </h4>
                <span className={styles.gamecard__teamscore}>{props.teams.loser.score}</span>
              </div>
            </div>
            <div className={styles.gamecard__overallrating}>
              <p>
                <span>Overall Rating</span>
                <span>{props.overall_rating}</span>
              </p>
            </div>
        </div>
    );
};

export default GameCard