// Image Gallery
// Add eventListener, on click remove DOM Element
// https://www.testdome.com/questions/javascript/image-gallery/62212?visibility=3&skillId=2&topicId=23

function setup() {
  buttons = document.getElementsByClassName("remove");
  for (let b of buttons) {
    b.addEventListener("click", function (e) {
      e.target.parentElement.remove();
    });
  }
}

// Example case.
document.body.innerHTML = `
<div class="image">
<img src="https://bit.ly/3lmYVna" alt="First">
<button class="remove">X</button>
</div>
<div class="image">
<img src="https://bit.ly/3flyaMj" alt="Second">
<button class="remove">X</button>
</div>`;

setup();

document.getElementsByClassName("remove")[0].click();
console.log(document.body.innerHTML);

// Customer List
// renders array of objects as list
// https://www.testdome.com/questions/javascript/topic-coloring/59267?visibility=3&skillId=2&topicId=23

function showCustomers(customers, targetList) {
  customers.forEach((item) => {
    let res = `
    <li>
        <p>${item.name}</p>;
        <p>${item.email}</p>;
    </li>
    `;
    targetList.innerHTML += res;
  });
}

document.body.innerHTML = `
<div>
    <ul id="customers">
    </ul>
</div>
`;
let customers = [
  { name: "John", email: "john@example.com" },
  { name: "Mary", email: "mary@example.com" },
];
showCustomers(customers, document.getElementById("customers"));

let customerParagraph = document.querySelectorAll("li > p")[0];
if (customerParagraph) {
  customerParagraph.click();
}
console.log(document.body.innerHTML);
