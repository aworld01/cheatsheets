const band = {
    bandName: "led zeppelin",
    famousSong: "stairway to heaven",
    year: 1948,
    anotherFamousSong: "kashmir",
    year: 2014
}

/* example1 */
// const bName = band.bandName;
// const fSong = band.famousSong;
// console.log(bName);
// console.log(fSong);


/* example2 */
// const {bandName, famousSong} = band;
// console.log(bandName);
// console.log(famousSong);


/* example3 */
// const {bandName: var1, famousSong: var2} = band;
// console.log(var1);
// console.log(var2);


/* example4 */
const {bandName, famousSong, ...restProps} = band;
console.log(bandName);
console.log(famousSong);
console.log(restProps);