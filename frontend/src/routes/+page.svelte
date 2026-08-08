<script>
    let aufgaben = $state([]);

    fetch("https://animated-pancake-wrrrw7r6jx5395wp-8000.app.github.dev/api/aufgaben/")
        .then(r => r.json())
        .then(data => {
            aufgaben = data;
        })
        .catch(err => {
            console.error(err);
        });
</script>

<h1>Aufgaben</h1>

{#if aufgaben.length === 0}
    <p>Keine Aufgaben gefunden.</p>
{:else}
    <ul>
        {#each aufgaben as a}
            <li>
                <strong>{a.titel}</strong><br>
                {a.beschreibung}
            </li>
        {/each}
    </ul>
{/if}


