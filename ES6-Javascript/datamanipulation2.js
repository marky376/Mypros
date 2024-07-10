const years = [];
years.push('mark', 'chelsea', 'stacy', 'tracy', 'gift', 'kristian', 'zaza');
years[8] = "Tina";

const iterator = years.keys();
for (const key of iterator) {
    console.log('${key}: ${years[key]}');
}

const newYears = years.toReversed();
