import unittest
from generate_test_step import GenerateTestStep


class TestGenerateTestStep(unittest.TestCase):
    def test_case2step(self):

        generate_step = GenerateTestStep()

        test_description = "Verify the button(Click me Green) triggers the expected click action."

        url = "https://seleniumbase.io/demo_page"

        web_content = '''
            <html lang="en">
                <head>
                    <title>Web Testing Page</title>
                    <meta property="og:site_name" content="Demo Page">
                    <meta property="og:title" content="Web Testing Page">
                    <meta name="Description" content="Test your automation framework here.">
                    <meta property="og:description" content="Test your automation framework here.">
                    <meta name="Keywords" content="Python, pytest, selenium, webdriver, test automation, testing, seleniumbase, test framework, HTML, JavaScript">
                    <meta property="og:keywords" content="Python, pytest, selenium, webdriver, test automation, testing, seleniumbase, test framework, HTML, JavaScript">
                    <meta property="og:image" content="https://seleniumbase.io/cdn/img/sb_demo_page.png">
                    <meta http-equiv="Content-Type" content="text/html, charset=utf-8">
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=0.41, shrink-to-fit=no">
                    <meta content="follow,index" name="robots">
                    <style>
                        html {
                            background-color: #9988ad;
                        }
                        html, body {
                            font-size: 100%;
                            box-sizing: border-box;
                        }
                        body {
                            background-image: none;
                            background-origin: padding-box;
                            background-color: #c6d6f0;
                            padding: 30;
                            margin: 10;
                            font-family: "Proxima Nova","proxima-nova",
                            "Helvetica Neue",Helvetica,Arial,sans-serif !important;
                            text-rendering: optimizelegibility;
                            -moz-osx-font-smoothing: grayscale;
                            box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.24),
                            1px 2px 12px 0px rgba(0, 0, 0, 0.18) !important;
                        }
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            border-spacing: 0;
                            box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.27),
                            1px 2px 12px 0px rgba(0, 0, 0, 0.21) !important;
                            transition: all 0.15s ease-out 0s;
                            transition-property: all;
                            transition-duration: 0.1s;
                            transition-timing-function: ease-out;
                            transition-delay: 0s;
                        }
                        table:hover {
                            box-shadow: 0px 2px 5px 1px rgba(0, 0, 0, 0.35),
                            1px 2px 12px 0px rgba(0, 0, 0, 0.28) !important;
                        }
                        thead th, thead td {
                            padding: 0.5rem 0.625rem 0.625rem;
                            font-weight: bold;
                            text-align: left;
                        }
                        thead {
                            text-align: center;
                            border: 1px solid #e1e1e1;
                            width: 150%;
                            color: #0C8CDF;
                            background-color: #c0f0ff;
                        }
                        tbody tr:nth-child(even) {
                            background-color: #f1f1f1;
                        }
                        tbody tr:nth-child(odd) {
                            background-color: #ffffff;
                        }
                        tbody tr:nth-child(even):hover {
                            background-color: #f8f8d2;
                        }
                        tbody tr:nth-child(odd):hover {
                            background-color: #ffffe0;
                        }
                        tbody th, tbody td {
                            padding: 0.5rem 0.625rem 0.625rem;
                        }
                        tbody {
                            border: 1px solid #e1e1e1;
                            background-color: #fefefe;
                        }
                        td {
                            padding: 5px 5px 5px 0;
                            vertical-align: top;
                        }
                        h1, h2, h3 {
                            text-align: center;
                            height: 32px;
                            margin: 2px;
                        }
                        h1 {
                            font-size: 24px;
                            color:#0066AA;
                        }
                        h2 {
                            color:#0B7CA7;
                        }
                        h3 {
                            color:#087B95;
                            font-size: 19px;
                        }
                        h1 table {
                            font-size: 27px;
                            text-align: left;
                            padding: 0.5rem 0.625rem 0.625rem;
                            font-weight: bold;
                            padding-right: 10px;
                            padding-left: 20px;
                            padding: 15px 15px 15px 0;
                        }
                        h2 table {
                            color: #0C8CDF;
                            font-size: 16px;
                            text-align: left;
                            font-weight: bold;
                            padding: 5px 5px 5px 0;
                            padding-right: 10px;
                            padding-left: 20px;
                        }
                        textarea {
                            font-family: "Proxima Nova","proxima-nova",
                            "Helvetica Neue",Helvetica,Arial,sans-serif !important;
                        }
                        button {
                            width: 94%;
                            font-size: 20px;
                        }
                        div.dropbtn {
                            width: 94%;
                            font-size: 17px;
                            text-align: center;
                            height: 23px;
                            padding: 3px 4px;
                            border: 1px solid #e1e1e1;
                        }
                        input {
                            font-size: 14px;
                        }
                        .dropbtn {
                            background-color: #4CAF50;
                            color: white;
                            width: 100%;
                            height: 30px;
                            padding: 2px 6px;
                            font-size: 17px;
                            border: 1px solid #e1e1e1;
                        }
                        .dropdown {
                            position: relative;
                            display: inline-block;
                            width: 100%;
                        }
                        .dropdown-content {
                            display: none;
                            position: absolute;
                            background-color: #f1f1f1;
                            width: 100%;
                            box-shadow: 0px 6px 12px 0px rgba(0,0,0,0.25);
                            z-index: 1;
                        }
                        .dropdown-content a {
                            color: black;
                            padding: 9px 16px;
                            text-decoration: none;
                            display: block;
                        }
                        .dropdown-content a:hover {
                            background-color: #cbdacb;
                        }
                        .dropdown:hover .dropdown-content {
                            display: block;
                        }
                        .dropdown:hover .dropbtn {
                            background-color: #3e8e41;
                        }
                        ul.horizontal {
                            list-style-type: none;
                            padding: 0;
                        }
                        ul.horizontal li {
                            display: inline;
                            background-color: lightblue;
                            padding: 0 5px;
                        }
                        tbody {
                            font-size: 11pt;
                        }
                        td.left {
                            text-align: right;
                        }
                        [contenteditable] {
                            border-style: solid;
                            border-width: 1px;
                        }
                        iframe.frameClass1 {
                            height: 26px;
                            width: 32px;
                            padding: 2px 2px 2px 2px;
                            color: #0C8CDF;
                            overflow:hidden;
                            background-color: #fefefe;
                            border: 2px solid #c1c1c1;
                        }
                        iframe.frameClass2 {
                            height: 26px;
                            width: 103px;
                            padding: 2px 2px 2px 2px;
                            border: none;
                            margin: none;
                            color: #0C8CDF;
                            overflow: hidden;
                            position: absolute;
                            background-color: #fefefe;
                            border: 2px solid #c1c1c1;
                        }
                        iframe.frameClass3 {
                            height: 28px;
                            width: 34px;
                            padding: 1px 1px 1px 1px;
                            border: none;
                            margin: none;
                            color: #0C8CDF;
                            overflow: hidden;
                            position: absolute;
                            background-color: #fefefe;
                            border: 2px solid #c1c1c1;
                        }
                        .slidecontainer {
                            width: 100%;
                        }
                        .slider {
                            -webkit-appearance: none;
                            width: 100%;
                            height: 20px;
                            background: #d3d3d3;
                            outline: none;
                            opacity: 0.7;
                            -webkit-transition: .2s;
                            transition: opacity .2s;
                        }
                        .slider:hover {
                            opacity: 1;
                        }
                        .slider::-webkit-slider-thumb {
                            -webkit-appearance: none;
                            appearance: none;
                            width: 16px;
                            height: 28px;
                            background: #4CAF50;
                            cursor: pointer;
                        }
                        .slider::-moz-range-thumb {
                            width: 16px;
                            height: 28px;
                            background: #4CAF50;
                            cursor: pointer;
                        }
                        #drop1,#drop2 {
                            width: 131px;
                            height: 21px;
                            padding: 1px;
                            border: 1.5px solid #aaaaaa;
                            background-color: #d6e6f0;
                        }
                        img:active {
                            box-shadow: 0px 2px 5px 1px rgba(105, 165, 155, 0.3),
                            1px 2px 12px 0px rgba(105, 165, 155, 0.2) !important;
                        }
                    </style>
                    <script async src="https://www.googletagmanager.com/gtag/js?id=G-P5KFWRNLRN"></script>
                    <script>
                      window.dataLayer = window.dataLayer || [];
                      function gtag(){dataLayer.push(arguments);}
                      gtag('js', new Date());
                      gtag('config', 'G-P5KFWRNLRN', { cookie_flags: 'SameSite=None;Secure' });
                    </script>
                </head>
                <body>
                    <!-- Tested with SeleniumBase - https://seleniumbase.io -->
                    <form id="myForm">
                        <table id="myTable" style="width: 804px; padding: 10px;">
                            <tbody id="tbodyId">
                                <tr>
                                    <td>
                                        <h1>Demo Page</h1>
                                    </td>
                                    <td>
                                        <h2>SeleniumBase</h2>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <div id="myDropdown" class="dropbtn" style="cursor: default;"
                                                    onclick="clickDropdownFunction()"
                                                    onmousemove="hoverDropdownFunction()">Hover Dropdown</div>
                                            <div class="dropdown-content" style="cursor: pointer;">
                                                <a id="dropOption1" onclick="clickLink1()">Link One</a>
                                                <a id="dropOption2" onclick="clickLink2()">Link Two</a>
                                                <a id="dropOption3" onclick="clickLink3()">Link Three</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <h3>Automation Practice</h3>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Text Input Field:</td>
                                    <td><input type="text" id="myTextInput"/></td>
                                    <td>Textarea:</td>
                                    <td style="padding: 6px 10px 6px 10px;">
                                        <textarea id="myTextarea" name="textareaName"
                                                  class="textareaClass area1" rows="2" cols="28"
                                                  style="resize: none; width: 94%; font-size: 14px;"></textarea>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Pre-Filled Text Field:</td>
                                    <td>
                                        <input type="text" value="Text..."
                                               id="myTextInput2" name="preText2"/>
                                    </td>
                                    <td>Button:</td>
                                    <td>
                                        <button onclick="buttonFunction1()" id="myButton" type="button"
                                                style="color: green;">Click Me (Green)</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Placeholder Text Field:</td>
                                    <td><input id="placeholderText" type="text"
                                               placeholder="Placeholder Text Field" /></td>
                                    <td>Read-Only Text Field:</td>
                                    <td>
                                        <input type="text" id="readOnlyText"
                                               value="The Color is Green"
                                               style="font-size: 19px; color: green; width: 94%;"
                                               readonly />
                                    </td>
                                </tr>
                                <tr>
                                    <td>HTML SVG with rect:</td>
                                    <td>
                                        <svg id="mySVG" name="svgName" width="154" height="20">
                                            <rect id="svgRect" width="154" height="20"
                                                  stroke="teal" stroke-width="4" fill="#4CA0A0">
                                                <animate attributeType="CSS" attributeName="opacity"
                                                         from="0.1" to="1" dur="1s" repeatCount="1"
                                                         restart="whenNotActive" />
                                                <animate attributeType="CSS" attributeName="width"
                                                         from="1" to="154" dur="1s" repeatCount="1"
                                                         restart="whenNotActive" />
                                            </rect>
                                        </svg>
                                    </td>
                                    <td><p>Paragraph with Text:</p></td>
                                    <td><p id="pText" style="color: green; font-size: 20px;">This Text is Green</p></td>
                                </tr>
                                <tr>
                                    <td>Input Slider Control:</td>
                                    <td>
                                        <input type="range" min="0" max="100" step="10"
                                               id="mySlider" name="sliderName" value="50"
                                               style="width: 88%;" class="slider"
                                               oninput="sliderFunction1()"
                                               onclick="sliderFunction1()"
                                               onchange="sliderFunction1()"
                                               onmousemove="sliderFunction1()"/>
                                    </td>
                                    <td><label id="progressLabel" for="progressBar">Progress Bar: (50%)</label></td>
                                    <td><progress id="progressBar" value="50" style="width: 94%;" max="100" /></td>
                                </tr>
                                <tr>
                                    <td>Select Dropdown:</td>
                                    <td>
                                        <select id="mySelect" name="selectName"
                                                class="selectClass" onchange="selectFunction1()"
                                                style="width: 95%; font-size: 14px;">
                                            <option value="25%">Set to 25%</option>
                                            <option value="50%">Set to 50%</option>
                                            <option value="75%">Set to 75%</option>
                                            <option value="100%">Set to 100%</option>
                                        </select>
                                    </td>
                                    <td><label id="meterLabel" for="meterBar">HTML Meter: (25%)</label></td>
                                    <td><meter id="meterBar" value="0.25" style="width: 94%;"></meter></td>
                                </tr>
                                <tr>
                                    <td><div style="color: #845342;">Image in iFrame:</div></td>
                                    <td style="padding: 4px 4px 3px 4px;">
                                        <iframe id="myFrame1" name="frameName1" class="frameClass1" scrolling="no"
                                        src='data:image/gif;base64,R0lGODlhEAAOALMAAOazToeHh0tLS/7LZv/0jvb29t/f3//Ub//ge8WSLf/rhf/3kdbW1mxsbP//mf///yH5BAAAAAAALAAAAAAQAA4AAARe8L1Ekyky67QZ1hLnjM5UUde0ECwLJoExKcppV0aCcGCmTIHEIUEqjgaORCMxIC6e0CcguWw6aFjsVMkkIr7g77ZKPJjPZqIyd7sJAgVGoEGv2xsBxqNgYPj/gAwXEQA7'></iframe>
                                        &nbsp;&nbsp;
                                        <iframe id="myFrame2" name="frameName2" class="frameClass2" scrolling="no"
                                        src="data:text/html,<body%20style=%22background-color:%23F2F6F8;%22>
                                        <h4>iFrame%20Text<%2Fh4></body>"></iframe>
                                    </td>
                                    <td>RadioButton 1:<input type="radio" checked id="radioButton1" 
                                                             name="radioGroup1" class="radioClass1"
                                                             style="width: 30px;"/>
                                    </td>
                                    <td>RadioButton 2:<input type="radio" id="radioButton2"
                                                             name="radioGroup1" class="radioClass1"
                                                             style="width: 30px;"/>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="width: 150px;">
                                        CheckBox:
                                        <input type="checkbox" id="checkBox1"
                                               name="checkBoxName1" class="checkBoxClassA"
                                               onchange="revealRow(event)"/>
                                    </td>
                                    <td style="width: 180px;">
                                        CheckBoxes:
                                        <input type="checkbox" id="checkBox2"
                                               name="checkBoxName2" class="checkBoxClassB"/>
                                        <input type="checkbox" id="checkBox3"
                                               name="checkBoxName3" class="checkBoxClassB"/>
                                        <input type="checkbox" id="checkBox4"
                                               name="checkBoxName4" class="checkBoxClassB"/>
                                    </td>
                                    <td style="width: 150px">
                                        Pre-Check Box:
                                        <input type="checkbox" id="checkBox5"
                                               name="checkBoxName5" class="checkBoxClassC" checked />
                                    </td>
                                    <td style="color: #845342; padding: 3px 3px 7px 9px; height: 38px;">
                                        CheckBox in iFrame:&nbsp;&nbsp;
                                        <iframe style="padding: 0px 0px 0px 0px;"
                                        id="myFrame3" name="frameName3" class="frameClass3" scrolling="no"
                                        src="data:text/html,
                                            <body%20style=%22background-color:%23F2F6F8;%22>
                                            <input%20type=%22checkbox%22%20id=%22checkBox6%22
                                            %20style=%22padding:%201px%201px%201px%201px;%22
                                            %20name=%22checkBoxName6%22
                                            %20class=%22checkBoxClassD%20fBox%22%20/>
                                            </body>"></iframe>
                                    </td>
                                </tr>
                                <tr style="display: none" class="hidden_row">
                                    <td>
                                        Drag and Drop A:
                                    </td>
                                    <td>
                                        <div id="drop1" class="dropzone" ondrop="drop(event)" ondragover="dragOver(event)" ondragenter="dragEnter(event)" ondragleave="dragLeave(event)"><img id="logo" src="https://seleniumbase.io/cdn/img/sb_logo_tiny.png" draggable="true" ondragstart="dragStart(event)" width="130" height="20"></div>
                                    </td>
                                    <td>
                                        Drag and Drop B:
                                    </td>
                                    <td>
                                        <div id="drop2" class="dropzone" ondrop="drop(event)" ondragover="dragOver(event)" ondragenter="dragEnter(event)" ondragleave="dragLeave(event)"></div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        URL Link:
                                    </td>
            
                                    <td>
                                        <a id="myLink1" name="linkName1" class="linkClass"
                                           href="https://seleniumbase.com">seleniumbase.com</a>
                                    </td>
                                    <td>
                                        Link with Text:
                                    </td>
            
                                    <td>
                                        <a id="myLink2" name="linkName2" class="linkClass"
                                           href="https://github.com/seleniumbase/SeleniumBase">
                                           SeleniumBase on GitHub</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        SeleniumBase Docs:
                                    </td>
            
                                    <td>
                                        <a id="myLink3" name="linkName3" class="linkClass"
                                           href="https://seleniumbase.io">seleniumbase.io</a>
                                    </td>
                                    <td>
                                        The Demo Page:
                                    </td>
            
                                    <td>
                                        <a id="myLink4" name="linkName4" class="linkClass"
                                           href="https://seleniumbase.io/demo_page/">
                                           SeleniumBase Demo Page</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </form>
                    <script>
                        function buttonFunction1() {
                          var x = document.getElementById("myButton");
                          var y = document.getElementById("pText");
                          var z = document.getElementById("readOnlyText");
                          if (x.style.color != "purple") {
                            x.style.color = "purple";
                            x.textContent = "Click Me (Purple)";
                            y.textContent = "This Text is Purple";
                            y.style.color = "purple";
                            z.value = "The Color is Purple";
                            z.style.color = "purple";
                          }
                          else {
                            x.style.color = "green";
                            x.textContent = "Click Me (Green)";
                            y.textContent = "This Text is Green";
                            y.style.color = "green";
                            z.value = "The Color is Green";
                            z.style.color = "green";
                          }
                        }
                    </script>
                    <script>
                        function sliderFunction1() {
                          var s = document.getElementById("mySlider");
                          var p = document.getElementById("progressBar");
                          var pl = document.getElementById("progressLabel");
                          p.value = s.value;
                          pl.textContent = "Progress Bar: (" + p.value + "%)";
                        }
                    </script>
                    <script>
                        function selectFunction1() {
                            var d = document.getElementById("mySelect").value;
                            var m = document.getElementById("meterBar");
                            var ml = document.getElementById("meterLabel");
                            if (d == "25%") {
                                m.value = "0.25";
                                ml.textContent = "HTML Meter: (25%)";
                            }
                            if (d == "50%") {
                                m.value = "0.5";
                                ml.textContent = "HTML Meter: (50%)";
                            }
                            if (d == "75%") {
                                m.value = "0.75";
                                ml.textContent = "HTML Meter: (75%)";
                            }
                            if (d == "100%") {
                                m.value = "1.0";
                                ml.textContent = "HTML Meter: (100%)";
                            }
                        }
                    </script>
                    <script>
                        function hoverDropdownFunction() {
                            overlay = document.querySelector(".dropdown-content");
                            overlay.style.pointerEvents = "auto";
                        }
                    </script>
                    <script>
                        function clickDropdownFunction() {
                            the_h3 = document.querySelector("h3");
                            the_h3.textContent = "Automation Practice";
                            overlay = document.querySelector(".dropdown-content");
                            overlay.style.pointerEvents = "none";
                        }
                    </script>
                    <script>
                        function clickLink1() {
                            the_h3 = document.querySelector("h3");
                            the_h3.textContent = "Link One Selected";
                            overlay = document.querySelector(".dropdown-content");
                            overlay.style.pointerEvents = "none";
                        }
                    </script>
                    <script>
                        function clickLink2() {
                            the_h3 = document.querySelector("h3");
                            the_h3.textContent = "Link Two Selected";
                            overlay = document.querySelector(".dropdown-content");
                            overlay.style.pointerEvents = "none";
                        }
                    </script>
                    <script>
                        function clickLink3() {
                            the_h3 = document.querySelector("h3");
                            the_h3.textContent = "Link Three Selected";
                            overlay = document.querySelector(".dropdown-content");
                            overlay.style.pointerEvents = "none";
                        }
                    </script>
                    <script>
                        document.getElementById("svgRect").addEventListener("click", evt => {
                            document.querySelectorAll("animate").forEach(element => {
                                element.beginElement();
                            });
                        });
                    </script>
                    <script>
                        function revealRow(event) {
                            // Show the Drag & Drop row if the first checkbox is checked.
                            if (event.target.checked)
                            {
                                document.querySelector('tr.hidden_row').style.display='';
                            }
                            else
                            {
                                document.querySelector('tr.hidden_row').style.display='none';
                            }
                        }
                    </script>
                    <script>
                        function dragOver(event) {
                            // Allow dropping.
                            event.preventDefault();
                        }
                        function dragEnter(event) {
                            event.preventDefault();
                            if ( event.target.className === "dropzone" ) {
                                event.target.style.background = "#c6b6d6";
                            }
                        }
                        function dragLeave(event) {
                            event.preventDefault();
                            if ( event.target.className === "dropzone" ) {
                                event.target.style.background = "#d6e6f0";
                            }
                        }
                        function dragStart(event) {
                            event.dataTransfer.setData("id_of_dragged_element", event.target.id);
                        }
                        function drop(event) {
                            event.preventDefault();
                            var data = event.dataTransfer.getData("id_of_dragged_element");
                            try {
                                event.target.appendChild(document.getElementById(data));
                                event.target.style.background = "#d6e6f0";
                            }
                            catch (HierarchyRequestError) {
                                // Drap & Drop to same location. Do nothing.
                            }
                        }
                    </script>
                </body>
            </html>
        '''

        result = generate_step.case2step(test_description=test_description, url=url, web_content=web_content)

        # 打印结果
        print("Generated Test Steps:")
        print(result)


if __name__ == "__main__":
    unittest.main()
