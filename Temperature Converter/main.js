function converter() {
  var celcius = document.querySelector(".cel-input").value;
  var farenheit = document.querySelector(".fra-input");
  var kelvin = document.querySelector(".kel-input");

  let Ftemp = (celcius * 9) / 5 + 32;
  let Ktemp = parseFloat(celcius) + 273.15;

  if (celcius === "") {
    farenheit.value = "";
  } else {
    farenheit.value = parseFloat(Ftemp.toExponential(4));
  }

  if (celcius === "") {
    kelvin.value = "";
  } else {
    kelvin.value = Ktemp.toExponential(4);
  }
}
