<template>
  <div class="app-container">
    <meta name="referrer" content="never" />
    <iframe :src="vscode_api"  frameborder="0" scrolling="auto" width="100%" height="950px" style="overflow-y:scroll;"></iframe>
  </div>
</template>

<script>
import {
  vscode_,
} from "@/api/code_server";

export default {
  name: "vscode_",
  data() {
    return {
      vscode_api: vscode_,
    };
  },
}
</script>


<style>
</style>
