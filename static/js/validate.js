function validate(submit) {
	var valid = true;
	var board = new Array(9);

	// creates board as 2d js array and resets color
	for (i = 0; i < 9; i++) {
		board[i] = new Array(9);
	}
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			board[j][i] = document.getElementsByName(j + "," + i)[0]["value"];
			document.getElementsByName(j + "," + i)[0].style.color = "black"
		}
	}

	var make_red = new Array(9);

	// checks accross
	for (i = 0; i < 9; i++) {
		var unique = new Array();
		for (j = 0; j < 9; j++) {
			if (board[i][j] != "") {
				unique.push(board[i][j])
			}
		}
		unique.sort();
		var red = new Array();
		last = 0;
		for (k = 0; k < unique.length - 1; k++) {

			if (unique[k] === unique[k + 1] && unique[k] != last) {
				red.push(unique[k]);
			}
			last = unique[k];
		}
		for (j = 0; j < 9; j++) {
			if (red.includes(board[i][j])) {
				make_red.push(j + "," + i)
				var element = document.getElementsByName(i + "," + j)[0]
				element.style.color = "red";
				valid = false;
			}
		}
	}


	// checks down
	for (i = 0; i < 9; i++) {
		var unique = new Array();
		for (j = 0; j < 9; j++) {
			if (board[j][i] != "") {
				unique.push(board[j][i])
			}
		}
		unique.sort();
		var red = new Array();
		last = 0;
		for (k = 0; k < unique.length - 1; k++) {
			if (unique[k] === unique[k + 1] && unique[k] != last) {
				red.push(unique[k]);
			}
			last = unique[k];
		}
		for (j = 0; j < 9; j++) {
			if (red.includes(board[j][i])) {
				make_red.push(j + "," + i)
				var element = document.getElementsByName(j + "," + i)[0]
				element.style.color = "red";
				valid = false;
			}
		}
	}

	// checks boxes
	for (k = 0; k < 3; k++) {
		for (l = 0; l < 3; l++) {
			var unique = new Array();
			for (i = k * 3; i < k * 3 + 3; i++) {
				for (j = l * 3; j < l * 3 + 3; j++) {
					if (board[j][i] != "") {
						unique.push(board[j][i])
					}
				}
			}
			unique.sort();
			var red = new Array();
			last = 0;
			for (i = 0; i < unique.length - 1; i++) {
				if (unique[i] === unique[i + 1] && unique[i] != last) {
					red.push(unique[i]);
				}
				last = unique[i];
			}
			for (i = k * 3; i < k * 3 + 3; i++) {
				for (j = l * 3; j < l * 3 + 3; j++) {
					if (red.includes(board[j][i])) {
						make_red.push(j + "," + i)
						var element = document.getElementsByName(j + "," + i)[0]
						element.style.color = "red";
						valid = false;

					}
				}
			}
		}
	}

	if (!valid) {
		if (submit) {
			alert("Please validate entries");
		}
		return false;
	}
	return true;
}