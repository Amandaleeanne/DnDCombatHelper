class Dice {
    static async random(min, max) {
        const url = `https://www.random.org/integers/?num=1&min=${min}&max=${max}&col=5&base=10&format=plain&rnd=new`;
        const response = await fetch(url);
        const number = await response.text();
        return parseInt(number);
    }

    static async d20(bonus) {
        const baseRoll = await Dice.random(1, 20);
        return [baseRoll, baseRoll + bonus];
    }

    static async d12(bonus) {
        const baseRoll = await Dice.random(1, 12);
        return [baseRoll, baseRoll + bonus];
    }

    static async d8(bonus) {
        const baseRoll = await Dice.random(1, 8);
        return [baseRoll, baseRoll + bonus];
    }

    static async d6(bonus) {
        const baseRoll = await Dice.random(1, 6);
        return [baseRoll, baseRoll + bonus];
    }

    static async d4(bonus) {
        const baseRoll = await Dice.random(1, 4);
        return [baseRoll, baseRoll + bonus];
    }

    static async diceRoll(bonus, diceNum) {
        const baseRoll = await Dice.random(1, diceNum);
        return [baseRoll, baseRoll + bonus];
    }
}