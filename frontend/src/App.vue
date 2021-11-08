<template>
  <div id="app">
    <router-view v-if="isRouterAlive"></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  provide() {
    return {
      reload: this.reload,
    };
  },
  data() {
    return {
      isRouterAlive: true,
    };
  },
  created() {
    console.log(
      `%c 写字楼里写字间，写字间里程序员；
          程序人员写程序，又拿程序换酒钱。`,
      "font-size:20px;color:red;"
    );
    // this.initWebSocket();
  },

  methods: {
    reload() {
      let that = this;
      that.isRouterAlive = false;
      that.$nextTick(function () {
        that.isRouterAlive = true;
      });
    },

    // initWebSocket() {
    //   let that = this;
    //   that.ws = new WebSocket(`ws://127.0.0.1:8000/ws`);
    //   that.global.setWs(that.ws);
    //   that.ws.onerror = that.websocketonerror;
    //   that.ws.onclose = that.websocketclose;
    // },

    // websocketonerror() {
    //   let that = this;
    //   that.initWebSocket();
    // },

    // websocketclose(e) {
    //   console.log("断开连接", e);
    // },
  },
};
</script>




<style>
@import "./assets/custom-theme/font.css";
* {
  font-family: PingFang;
}
</style>