
d3.csv("static/cities.csv", function(data) {

// Append to website
    d3.select("tbody")
    .selectAll("tr")
    .data(data)
    .enter()
    .append("tr")
    .html(function(d) {
      return `<td>${d.City_ID}</td><td>${d.City}</td><td>${d.Cloudiness}</td>
      <td>${d.Country}</td><td>${d.Date}</td><td>${d.Humidity}</td>
      <td>${d.Lat}</td><td>${d.Lng}</td><td>${d.Max_Temp}</td><td>${d.Wind_Speed}</td>`;
    });
});