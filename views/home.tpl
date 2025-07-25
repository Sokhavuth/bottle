% rebase('layout.tpl')
<section class="region">
<pre>
<code>print('Hello')
print('Hello')
</code>
</pre>
<div id="output-area"></div>
<py-script>
    from pyscript import display
    display("Hello from PyScript!", target="output-area")
</py-script>
</section>

<style>
    .hljs-ln-numbers { /* Target the line number container */
        padding-right: 10px !important; /* Adjust as needed */
    }
    .hljs-ln-code { /* Target the code container */
        margin-left: 10px !important; /* Adjust as needed */
    }
</style>