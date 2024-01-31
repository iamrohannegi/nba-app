import { useContext } from "react";
import ScoreContext from "../store/score-context";
import styles from './ScoreToggler.module.css';

const ScoreToggler = () => {
    const scoreCtx = useContext(ScoreContext)

    const handleCheckbox = (event) => {
        scoreCtx.handleScoreVisibilityChange(event.currentTarget.checked)
    }

    return (
        <div className={styles.toggler}>
            <span>Show Scores</span>
            <div>
                <input type="checkbox" id="switch" onChange={handleCheckbox} />
                <label for="switch">Toggle</label>
            </div>
        </div>


    )
}

export default ScoreToggler;