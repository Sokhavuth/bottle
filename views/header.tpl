<section class='Header'>
    <div class="inner region">
        <div class='logo'>
            <a href='/'><img  src="/static/images/python-logo.png" /></a>
            <a class="letter" href="/">{{data['siteTitle']}}</a>
        </div>
        <div class="search"><input type="text" /><input type="button" value="Search" /></div>
        <div class="login"><a href="/admin">Login</a> | <a href="/admin/user">Register</a></div>
    </div>
</section>

<style>
.Header{
    background: var(--background-dark);
}
.Header .inner{
    display: grid;
    grid-template-columns: 40% auto 20%;
    align-items: center;
}
.Header .inner .logo{
    position: relative;
    display: grid;
    grid-template-columns: 100px auto;
    align-items: center;
}
.Header .logo img{
    width: 100%;
}
.Header .logo .letter{
    position: absolute;
    font: 50px/1.5 Lobster, Bayon;
    color: var(--color);
    top: 10%;
    left: 22%
}
.Header .search{
    display: grid;
    grid-template-columns: auto 20%;
}
.Header .search input{
    padding: 1px 5px;
    font: var(--body-font)
}
.Header .login{
    text-align: right;
}
.Header .login a{
    color: var(--color);
}
</style>