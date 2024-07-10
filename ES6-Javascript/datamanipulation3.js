function method(callbackFn, thisArg) {
    const length = this.length;
    for (let i = 0; i < length; i++) {
        if (i in this) {
            const result = callbackFn.call(thisArg, this[i], i, this);
            // Do something with the result; maybe return early
        }
    }
}

// iterative methods in js
