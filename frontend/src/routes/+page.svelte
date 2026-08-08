<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>

<script>
    let msg = $state("Lade…");

    fetch("https://animated-pancake-wrrrw7r6jx5395wp-8000.app.github.dev/")
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

