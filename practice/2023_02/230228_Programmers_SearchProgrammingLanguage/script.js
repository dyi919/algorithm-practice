const $SelectedLanguage = document.querySelector(".SelectedLanguage");
const $SelectedLanguage__ul = document.querySelector(".SelectedLanguage ul");
const $SearchInput = document.querySelector(".SearchInput");
const $SearchInput__input = document.querySelector(".SearchInput__input");
const $Suggestion = document.querySelector(".Suggestion");
const $Suggestion__ul = document.querySelector(".Suggestion ul");

let isSuggestionOpen = false;
let suggestionList = [];
let selectedList = [];

$SearchInput.addEventListener("submit", (e) => {
  e.preventDefault();
});

$Suggestion.style.display = "none";

function resetSuggestion() {
  suggestionList = [];
  $Suggestion.style.display = "none";
  isSuggestionOpen = false;
  return;
}

$SearchInput__input.addEventListener("input", async () => {
  const searchParam = $SearchInput__input.value;

  if (searchParam.length === 0) {
    resetSuggestion();
    return;
  }

  const response = await fetch(
    `https://wr4a6p937i.execute-api.ap-northeast-2.amazonaws.com/dev/languages?keyword=${searchParam}`
  );
  const data = await response.json();
  if (data.length === 0) {
    resetSuggestion();
    return;
  }

  let frag = document.createDocumentFragment();
  for (let i = 0; i < data.length; i++) {
    const li = document.createElement("li");
    const span = document.createElement("span");

    const matchIndex = getMatchIndex(data[i], searchParam);

    span.textContent = data[i].slice(
      matchIndex,
      matchIndex + searchParam.length
    );
    span.className = "Suggestion__item--matched";

    li.textContent =
      data[i].slice(0, matchIndex) +
      data[i].slice(matchIndex + searchParam.length);
    if (li.textContent)
      li.insertBefore(span, li.childNodes[0].splitText(matchIndex));
    else li.appendChild(span);

    if (i === 0) li.classList.add("Suggestion__item--selected");
    frag.appendChild(li);
  }

  suggestionList = data;
  $Suggestion__ul.innerHTML = "";
  $Suggestion__ul.appendChild(frag);
  $Suggestion.style.display = "block";
  isSuggestionOpen = true;
});

function getMatchIndex(word, searchParam) {
  const wordLower = word.toLowerCase();
  const searchParamLower = searchParam.toLowerCase();

  return wordLower.indexOf(searchParamLower);
}
