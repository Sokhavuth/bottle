% rebase('layout.tpl')
<section class="Home region">
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
<script src="/static/scripts/ckeditor4/ckeditor.js"></script>
<form>
    <textarea name="editor1" id="editor1" rows="10" cols="80">
        This is my textarea to be replaced with CKEditor 4.
    </textarea>
    <script>
        // Replace the <textarea id="editor1"> with a CKEditor 4
        // instance, using default configuration.
        CKEDITOR.replace( 'editor1' );
    </script>
        </form>
</section>

<style>
    .hljs-ln-numbers { /* Target the line number container */
        padding-right: 10px !important; /* Adjust as needed */
    }
    .hljs-ln-code { /* Target the code container */
        margin-left: 10px !important; /* Adjust as needed */
    }
</style>