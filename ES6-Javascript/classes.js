class Area {
    constructor(s1, s2) {
        this.s1 = s1;
        this.s2 = s2;
    }
    
}

class Square extends Area {
    
    constructor(s1, s2) {
        super(s1, s2);
    }
    getArea(){
    
        return this.s1 * this.s2;
    }
}

class Rectangle extends Square {
    constructor(s1, s2) {
        super(s1, s2);
    }
    
    getArea1() {
        return this.s1 * this.s2;
    }
}

const mn = new Square(10, 10);
console.log(mn.getArea());

const mn2 = new Rectangle(10, 10);
console.log(mn2.getArea1());

