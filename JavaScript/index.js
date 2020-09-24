/**
 * @param {Number} hours
 * @param {Number} minutes
 * @param {Number} interval
 * @returns {String}
 */
module.exports = function (hours, minutes, interval) {
	
	//	hours_input = min_input/60 % 24
	//	minutes = min_input % 60
	//	print(int(hours), int(minutes))
	//  print (int (A * N + (B * N / 100)), B * N % 100)

	hours = Math.floor ((hours + (minutes+interval) / 60)%24);
	minutes = (minutes + interval) % 60;

	if (hours < 10) {
		hours= '0' + String(hours)
	};

	if (minutes < 10) {
		minutes = '0' + String(minutes)
	};

	if (minutes == 0 || minutes == 60) {
		minutes = '00';
	};

	if (hours == 0 || hours % 24 == 0) {
		hours = '00';
	};

	var result= String (hours)+':'+ String (minutes);

	return result;
};
