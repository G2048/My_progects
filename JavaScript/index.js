/**
 * @param {Number} hours
 * @param {Number} minutes
 * @param {Number} interval
 * @returns {String}
 */
module.exports = function (hours_input, min_input, interval) {
	var hours;
	var minutes_1 = minutes+interval;

	
//	hours_input = min_input/60 % 24
//	minutes = min_input % 60
//	print(int(hours), int(minutes))
//print (int (A * N + (B * N / 100)), B * N % 100)


	if (0 <= minutes_1 && minutes_1<=59) {
		minutes= minutes + interval
	}
	if (minutes_1==60) {
			minutes= '00';
			hours = hours+1;
		}
    if (minutes_1>60) {
    	minutes= minutes+ (minutes_1%60);
    	hours = Math.floor (minutes_1/60) + hours

    }

	if (0<= hours && hours <=23 && minutes_1!=60) {
		hours= hours + Math.floor (minutes_1/60)
	}
	if (hours==24) {
		hours = '00';
	}		
	

	var result= String (hours)+':'+ String (minutes);
	console.info (result)

	return result;
};
