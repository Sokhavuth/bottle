<section class="Menu">
    <nav class="region">
        <div class="topnav">
            <a href="/">Home</a>
            <a href="/about">About</a>
        </div>
    </nav>
</section>

<style>
.Menu{
    background: var(--menu);
}
.Menu .region .topnav {
    background-color: var(--menu);
    overflow: hidden;
}
.Menu .region .topnav a{
    float: left;
    color: var(--color);
    display: block;
    text-align: center;
    padding: 5px 10px;
}
.Menu .region .topnav a:hover{
    background: #0a0e11;
}
.Menu .region .topnav a.active{
    background: #0a0e11;
}
</style>