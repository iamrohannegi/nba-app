import { useContext } from "react";
import ScoreContext from "../store/score-context";

const ScoreToggler = () => {
    const scoreCtx = useContext(ScoreContext)

    const handleCheckbox = (event) => {
        scoreCtx.handleScoreVisibilityChange(event.currentTarget.checked)
    }

    return (
        <input type="checkbox" onChange={handleCheckbox} /> 
    )
}

export default ScoreToggler;