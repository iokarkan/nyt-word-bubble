let currentUrl = dayUrl;
const outer_container = document.getElementById("container")
const wordBubble = document.getElementById("word-bubble");

function createWordBubble(words) {
  const width = wordBubble.getBoundingClientRect().width;
  const height = wordBubble.getBoundingClientRect().height;

  const container = d3.select("#word-bubble");

  // Clear the existing SVG contents
  container.select("svg").remove();

  const svg = container
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  const wordLayout = d3
    .layout.cloud()
    .size([width, height])
    .words(words)
    .padding(5)
    .rotate(() => ~~(Math.random() * 2) * 90)
    .fontSize((d) => d.size)
    .on("end", draw);

  wordLayout.start();

  function draw(words) {
    svg
      .selectAll("text")
      .data(words)
      .enter()
      .append("text")
      .style("font-size", (d) => d.size + "px")
      .style("fill", "#333")
      .attr("text-anchor", "middle")
      .attr("transform", (d) => `translate(${[d.x, d.y]}) rotate(${d.rotate})`)
      .text((d) => d.text);
  }
}

function fetchWordBubbleData() {
  fetch(currentUrl) // Fetch data based on the selected view
    .then((response) => response.json())
    .then((data) => {
      if (data.length > 0) {
        const words = data.map((item) => ({
          text: item.word,
          size: item.frequency * 10, // you might want to adjust this scaling factor
        }));
        createWordBubble(words);
      } else {
        setTimeout(fetchWordBubbleData, 5000); // Retry after 5 seconds
      }
    });
}

function handleToggleChange() {
  const toggle = document.getElementById("toggle");
  const toggleBall = document.getElementById("toggleBall");
  const toggleLabel = document.getElementById("toggleLabel");
  const toggleButtonLabel = document.getElementById("toggleButtonLabel");
  const selectedView = toggle.checked ? "week" : "day";

  if (selectedView === "day") {
    currentUrl = dayUrl;
    toggleLabel.textContent = "Yesterday";
  } else if (selectedView === "week") {
    currentUrl = weekUrl;
    toggleLabel.textContent = "Last week";
  }

  // Animate the toggle ball
  toggleBall.classList.toggle("translate-x-6");
  if (toggleButtonLabel.classList.contains("bg-indigo-300")) {
    toggleButtonLabel.classList.remove("bg-indigo-300");
    toggleButtonLabel.classList.add("bg-indigo-700");
  }
  else {
    toggleButtonLabel.classList.add("bg-indigo-300");
    toggleButtonLabel.classList.remove("bg-indigo-700");
  }

  setTimeout(() => {
    window.onresize = fetchWordBubbleData; // handle window resizing
    fetchWordBubbleData();
  }, 500);
}

document.getElementById("toggle").addEventListener("change", handleToggleChange);

window.onresize = fetchWordBubbleData; // handle window resizing
fetchWordBubbleData();
