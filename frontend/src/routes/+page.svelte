<script>
    let counter = 0

    const handleCounter = () => {
        counter += 1
    }
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<p>{counter}</p>
<button on:click={handleCounter}>Counter</button>
<p>Visit <a href="/about">about</a> to read the about page</p>
<p></p>
