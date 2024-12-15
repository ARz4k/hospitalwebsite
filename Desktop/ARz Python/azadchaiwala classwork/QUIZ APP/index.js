const dataset = [
  {
    question : 'what is the full form of HTML',
    option : ['Hyper Text Markup Language','High Tech Mark Language','High Text Markup Language','Hyper Text Machine Language'],
    answer:'Hyper Text Markup Language'
  },
  {
    question : 'Which CSS property is used to set the background color of an element?',
    option : ['color','background-color','bgcolor','background'],
    answer:'background-color'
  },
  {
    question : 'What is the purpose of JavaScript in web development?',
    option : ['To style web pages','To create web page layouts','To add interactivity to web pages','To manage databases'],
    answer:'To add interactivity to web pages'
  },
  {
    question : 'Which of the following is a semantic HTML element?',
    option : ['div','span','header','p'],
    answer:'header'
  },

]

function Options(option_text, i) {
  const options_container = document.querySelector(".option");
  const input = document.createElement("input");
  input.setAttribute("type", "radio");
  input.setAttribute("name", "option");
  input.setAttribute("value", option_text);
  input.setAttribute("id", `option_${i}`);

  const label = document.createElement("label");
  label.setAttribute("for", `option_${i}`);
  options_container.append(input, label);
  label.innerText = option_text;
}

 let index = 0;

 function startQuiz(){
    index=0;
    displayQuestion();

 }

function displayQuestion() {
  const options_container = document.querySelector(".option");
  options_container.innerHTML = "";
 let dataset_question = dataset[index];
 const question_el = document.querySelector('#question')
 question_el.innerHTML = dataset_question["question"]

 const option_set = dataset_question['option'];

  for (let i = 0; i < option_set.length; i++) {
    let text = option_set[i];
    Options(text, i);
  }
}

function handleSubmit(e) {
    e.preventDefault()
const user_ans = e.target.option.value;
const dataset_question = dataset[index];
const checked = document.querySelector('input:checked')
const label = checked.nextElementSibling;
if(user_ans === dataset_question.answer){
label.classList.add('correct')

}
else{
  label.classList.add('incorrect')
}
    

    setTimeout(()=>{
        index++;
        if(index<dataset.length){
          displayQuestion()
        }
        else{
          startQuiz()
        }
    },500)
}

const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);

startQuiz()