<!--views/base.tpl-->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{{data['pageTitle']}}</title>
    <script src="/static/scripts/jQuery.js"></script>
    <link href="/static/images/siteLogo.png" rel="icon" ></link>
    <link href="/static/fonts/setup.css" rel="stylesheet"></link>
    <link href="/static/styles/base.css" rel="stylesheet"></link>
    <link rel="stylesheet" href="/static/scripts/pyscript/core.css"></link>
    <script type="module" src="/static/scripts/pyscript/core.js"></script>
    <link rel="stylesheet" href="/static/scripts/highlight/styles/default.css">
    <script src="/static/scripts/highlight/highlight.min.js"></script>
    <script src="/static/scripts/highlightjs-line-numbers.min.js"></script>
    
  </head>
  <body>
    {{!base}}
    <script>
      hljs.highlightAll()
      hljs.initLineNumbersOnLoad()
    </script>
  </body>
</html>