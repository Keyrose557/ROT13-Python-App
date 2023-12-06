
# ROT Cipher App

This application provides an intuitive interface for encoding and decoding text using the ROT13 cipher, a straightforward letter substitution cipher that substitutes a letter with the 13th letter following it in the alphabet. Developed in Python and utilizing the Tkinter library for its graphical user interface, the app exemplifies Python's flexibility in managing string manipulations and crafting GUI components. Additionally, it features an adjustable shift function, allowing users to select their desired substitution shift value, enhancing interaction and utility.

![Rot App Demo](/media/rot_test.gif)

---

## Student Notes

In this section, I share a collection of personal notes and insights gathered during the development of the ROT Encoder/Decoder App.They offer a broad behind-the-scenes glimpse into the process I used for my academic project 🤓. Feel free to explore these notes.The application, source code, and a jupyter notebook references are in the `dist` folder.

---

### Tools used

- [ ] [Python](https://www.python.org/downloads/)
- Add to Path when installing
- [ ] [VScode](https://code.visualstudio.com/)

VScode Extensions: I found helpful

- Code Spell Checker
- indent-rainbow
- Trailing Spaces
- Prettier-Code
- Python Extension Pack
- Jupyter
- Jupyter PowerToys

---

### Python Environment Setup in VScode

#### 1. Create a Workspace for your Python Project

Using VScode, Create a folder to store all your files

![Example](/media/ex1.gif)

This will be our workspace for our project. Name the folder to your preference and use folders as needed to keep the project organized and tidy. :)

---

#### 2. Create a Virtual Environment for your Project

- In VScode, use `Ctrl+Shift+P` and pick `Python:Create Environment`
- Using the `venv` option
- VScode will ask if you want to allow the virtual environment in your folder select `Yes`

![Example2](/media/ex2.PNG)

You should now be able to add/download Packages exclusively for our Project using VScode integrated Terminal.

Taking advantage of Python's built-in Virtual Environment module `.venv`, we can keep our Project's Python Packages contained inside The Project folder and manage them without interfering with other projects.

**Using `pip` to Install Packages**

- `pip` is Python's default Package Manager, This is how we add external libraries to expand Python's capabilities to meet our Project needs.

Example:

```bash

pip install package_name
```

![Example2g](/media/ex2.gif)

##### Installed Packages

- [ ] `ipykernel`
  - For Jupyter Notebook support in VScode, not required for project
- [ ] `pyinstaller`
  - For compiling Source Code into a Single Executable program

---

**3. Test basic functionality**.

Ensure your workspace can Execute code and Utilize Python's Package Manager `pip`. **However**, I highly recommend using a virtual Python environment to keep your project contained when it comes to package management for the project.

![Example1g](/media/ex1.PNG)

Its always a good idea to ensure you have a functioning environments for your project. Performing a function test will save us some headaches when troubleshooting.

---

#### You Ready to start coding your Python Project :)

Resource: [Python for Everybody](https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_(Severance))

---

### Creating the App

#### 4. Use Tkinter to make GUI

Once the functionality of the source code is working as intended. Create a Graphical User Interface(GUI) for users. Tkinter is built in python for a simple an fast GUI setup, its beginner friendly.

Resource: [Tkinter GUI](https://realpython.com/python-gui-tkinter/)

---

#### 5. Use `pyinstaller` to create the Executable

After finishing the source code and GUI use pyinstaller to test and demo the app on other devices. Be aware of pyinstaller limitaions [here](https://python.land/deployment/pyinstaller#Limitations)

Resource: [Pyinstaller](https://python.land/deployment/pyinstaller)

Command Used:

```bash

pyinstaller --onefile --windowed rot.py
```

---

#### 6. Revise

After demoing the App, revise the App and explore on making it better.

---

### Tips

If you followed this outline, here are some tips that have helped me as a student.

#### Jupyter Notebooks

I used Jupyter Notebook to practice and learn Coding concepts. Its a notebook for your code, where we can see the immediate results of code. This is helpful for collaboration and student comprehension. Try it out :)

>Select the `.venv` you created for this project as the kernel, if prompted when using a jupyter noteboook along side the project. When creating one, save as a `.ipynb` file.

![Example4](/media/ex4.PNG)

---

### Common **Troubleshooting** Steps

- [ ] Verify python install

```bash

python -V
```

>Checks installed Python version

- Not installed? Install [Python](https://www.python.org/downloads/)

- [ ] Powershell by default disables running scripts

- Try `Command Prompt`

- [ ] Python wont execute on CMD after install

- [Add Python to Path Manually](https://www.mygreatlearning.com/blog/add-python-to-path/)

---

## Resources

Resource 1: [Setup Python Environment in VScode](https://code.visualstudio.com/docs/python/environments)

- Guidance on settings up a Python Environment in VScode.

Resource 2: [Juypter Notebooks in VScode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

- Guidance on using Juypter on VScode. This section [here](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) I found the most helpful.

Resource 2: [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

- Quick Reference for Markdown

Resource 3: [Python for Everybody](https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Python_for_Everybody_(Severance))

- Free Python Book

Resource 4: [Pyinstaller](https://python.land/deployment/pyinstaller)

- A short read for creating a Python Executable using pyinstaller

Resource 4: [Tkinter GUI](https://realpython.com/python-gui-tkinter/)

- Tkinter references for GUI

Resource 5: [Python Standard Library](https://docs.python.org/3/library/index.html)

- Info on what is included in Python by default
