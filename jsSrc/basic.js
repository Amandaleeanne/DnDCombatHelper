// Assume Dice.d20 and Dice.d4 are implemented elsewhere
import Dice from './roller.js'
// Basic Spellcasting----------------------------------------
function spellcast(bonus) {
    let roll = Dice.d20(bonus);
    if (roll[1] >= 12) {
        return `Success! Total ${roll[1]}, base ${roll[0]}`;
    } else if (roll[1] < 12 && roll[0] !== 1) {
        return `Fail ${roll[1]}. Forget spell, Disapproval increased`;
    } else {
        return `Fail ${roll[0]}! Corruption!`;
    }
}

// Attack -----------------------------------------------------
function attack(bonus, warrior) {
    let roll = Dice.d20(bonus);
    let featSuccess = false;
    // insert natural crit and fumble here.
    if (warrior) {
        let feat = Dice.d4(4);
        let total = roll[1] + feat[1];
        if (feat[0] >= 3) {
            featSuccess = true;
        }
        if (featSuccess) {
            return `Feat succeeded ${feat}. Total ${total}, die roll ${roll[0]}, bonus ${bonus}`;
        } else {
            return `Feat failed ${feat}. Total ${total}, die roll ${roll[0]}, bonus ${bonus}`;
        }
    }
    return `Rolled a ${roll[1]}, die roll ${roll[0]}`;
}

function main() {
    let exit = false;
    while (!exit) {
        let validInput = ["y", "n", "Y", "N", "attack", "a", "spell", "spellcast", "s"];
        let spellInputs = ["spell", "spellcast", "s"];
        let attackInputs = ["attack", "a"];
        let warrior = false;

        let user = prompt("What do you want to do? (a)ttack/(s)pell: ").trim();
        let bonus = parseInt(prompt("bonus: "));
        console.log("\n");

        if (validInput.includes(user)) {
            if (spellInputs.includes(user)) {
                console.log(spellcast(bonus));
            } else {
                user = prompt("Warrior? (y/n): ").trim();
                warrior = user.toLowerCase() === "y";
                console.log(attack(bonus, warrior));
            }

            // Exit case
            user = prompt("Do you want to exit? (y/n): ");
            console.log("\n");
            if (user.toLowerCase() === "y") {
                exit = true;
            }
        } else {
            console.log("Invalid input\n");
        }
    }
}

main();
