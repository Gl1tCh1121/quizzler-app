<h1 align="center">Python Quiz App</h1>

<p>
  A simple Python-based quiz application with a graphical interface.<br>
  <br>
  Test your knowledge and track your score as you answer questions!
</p>

<hr>

<h2> Features</h2>
<ul>
  <li><b>Quiz questions available:</b>
    <ul>
      <li><b>Multiple-choice questions</b> – answer questions and get immediate feedback.</li>
      <li><b>True/False questions</b> – simple yes/no questions.</li>
    </ul>
  </li>
  <li><b>Score tracking:</b>
    <ul>
      <li>Correct answers count</li>
      <li>Total questions answered</li>
      <li>Final score displayed at the end</li>
    </ul>
  </li>
  <li><b>Interactive GUI</b> with buttons for selecting answers.</li>
</ul>

<hr>

<h2>Project Structure</h2>

<pre>
📦 quizzler
 ┣ 📦 images
  ┣ true.png
  ┣ false.png
 ┣ 📂 ui.py             # GUI code for displaying questions & handling user input
 ┣ 📜 data.py           # Contains the question data
 ┣ 📜 question_model.py # Question class storing question text & answer
 ┣ 📜 quiz_brain.py     # Core quiz logic & score tracking
 ┣ 📜 main.py           # Launches the quiz app
</pre>

<hr>

<h2> Getting Started</h2>

<h3>1. Clone the repository</h3>

<h3>2. Install dependencies</h3>
<pre><code>pip install tkinter
pip install requests
</code></pre>

<h3>3. Run the app</h3>
<pre><code>python main.py
</code></pre>

<hr>

<h2> Example Usage</h2>
<pre>
Question 1: What is the capital of France?
> User selects: Paris
✅ Correct!

Question 2: Is Python a programming language?
> User selects: True
✅ Correct!

You've completed the quiz
Your final score was: 2/2
</pre>

<hr>

<h2> Built With</h2>

<ul>
  <li>Python 3.9+</li>
  <li>Tkinter (for GUI)</li>
</ul>

<hr>

<h2> Future Plans</h2>
<ul>
  <li>Add multiple difficulty levels</li>
  <li>Support for more question types (fill-in-the-blank, multiple correct answers)</li>
  <li>Save high scores locally</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! If you'd like to improve the quiz app, follow these steps:</p>
<ol>
  <li>Fork the repository</li>
  <li>Create a new branch</li>
  <li>Commit your changes</li>
  <li>Push to your branch</li>
  <li>Open a Pull Request</li>
</ol>
<hr>

