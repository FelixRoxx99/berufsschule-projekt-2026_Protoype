<script>
    let msg = "Lade…";

    fetch("https://animated-pancake-xxxxxx-8000.app.github.dev/")
        .then(r => r.json())
        .then(data => {
            msg = data.msg;
        })
        .catch(err => {
            msg = "Fehler beim Laden der API";
            console.error(err);
        });
</script>

<h1>{msg}</h1>

