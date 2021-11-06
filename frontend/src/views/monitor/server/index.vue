<template>
  <div class="app-container">
    <el-row>
      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span style="width: 100%; font-weight:bold;">CPU</span></div>
          <div
            v-loading="loading"
            class="el-table el-table--enable-row-hover el-table--medium"
          >
            <table cellspacing="0" style="width: 100%; font-weight:bold;">
              <thead>
              <tr>
                <th class="is-leaf">
                  <div class="cell">属性</div>
                </th>
                <th class="is-leaf">
                  <div class="cell">值</div>
                </th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  <div class="cell">核心数</div>
                </td>
                <td>
                  <div v-if="server.cpu" class="cell">
                    {{ server.cpu.cpuNum }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">用户使用率</div>
                </td>
                <td>
                  <div v-if="server.cpu" class="cell">
                    {{ server.cpu.used }}%
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">进程数</div>
                </td>
                <td>
                  <div v-if="server.cpu" class="cell">
                    {{ server.cpu.pids }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">系统使用时间</div>
                </td>
                <td>
                  <div v-if="server.cpu" class="cell">
                    {{ server.cpu.boot_time }}H
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span style="width: 100%; font-weight:bold;">内存</span></div>
          <div
            v-loading="loading"
            class="el-table el-table--enable-row-hover el-table--medium"
          >
            <table cellspacing="0" style="width: 100%; font-weight:bold;">
              <thead>
              <tr>
                <th class="is-leaf">
                  <div class="cell">属性</div>
                </th>
                <th class="is-leaf">
                  <div class="cell">值</div>
                </th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  <div class="cell">总内存</div>
                </td>
                <td>
                  <div v-if="server.mem" class="cell">
                    {{ server.mem.total }}G
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">已用内存</div>
                </td>
                <td>
                  <div v-if="server.mem" class="cell">
                    {{ server.mem.used }}G
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">剩余内存</div>
                </td>
                <td>
                  <div v-if="server.mem" class="cell">
                    {{ server.mem.free }}G
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">使用率</div>
                </td>
                <td>
                  <div
                    v-if="server.mem"
                    class="cell"
                    :class="{ 'text-danger': server.mem.percent > 80 }"
                  >
                    {{ server.mem.percent }}%
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span style="width: 100%; font-weight:bold;">Redis</span></div>
          <div
            v-loading="loading"
            class="el-table el-table--enable-row-hover el-table--medium"
          >
            <table cellspacing="0" style="width: 100%; font-weight:bold;">
              <thead>
              <tr>
                <th class="is-leaf">
                  <div class="cell">属性</div>
                </th>
                <th class="is-leaf">
                  <div class="cell">值</div>
                </th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  <div class="cell">操作系统</div>
                </td>
                <td>
                  <div class="cell">{{ redisData.os }}</div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">版本信息</div>
                </td>
                <td>
                  <div class="cell">
                    {{ redisData.version }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">开放端口</div>
                </td>
                <td>
                  <div v-if="redisData.port" class="cell">
                    {{ redisData.port }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">已用内存</div>
                </td>
                <td>
                  <div
                    class="cell"
                    :class="{
                        'text-danger': redisData.used_memory_human > 80,
                      }"
                  >
                    {{ redisData.used_memory_human }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">内存占用峰值</div>
                </td>
                <td>
                  <div class="cell" :class="{ 'text-danger': 'true' }">
                    {{ redisData.used_memory_peak_human }}
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12" class="card-box">
        <el-card>
          <div slot="header"><span style="width: 100%; font-weight:bold;">MongoDB</span></div>
          <div
            v-loading="loading"
            class="el-table el-table--enable-row-hover el-table--medium"
          >
            <table cellspacing="0" style="width: 100%; font-weight:bold;">
              <thead>
              <tr>
                <th class="is-leaf">
                  <div class="cell">属性</div>
                </th>
                <th class="is-leaf">
                  <div class="cell">值</div>
                </th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>
                  <div class="cell">版本信息</div>
                </td>
                <td>
                  <div v-if="mongoData.version" class="cell">
                    {{ mongoData.version }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">总运行时长</div>
                </td>
                <td>
                  <div v-if="mongoData.uptime" class="cell">
                    <b>{{ mongoData.uptime }}</b>
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">活跃连接数</div>
                </td>
                <td>
                  <div v-if="mongoData.connections" class="cell">
                    {{ mongoData.connections.active }}
                  </div>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="cell">数据库集合</div>
                </td>
                <td>
                  <div
                    v-if="mongoData.collections"
                    class="cell"
                    :class="{ 'text-danger': 'true' }"
                  >
                    {{ mongoData.collections }}
                  </div>
                </td>
              </tr>

              <tr>
                <td>
                  <div class="cell">数据库文档</div>
                </td>
                <td>
                  <div class="cell" :class="{ 'text-danger': 'true' }">
                    {{ mongoData.objects }}
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {get_redis_data, get_mongo_data} from "@/api/monitor";
import io from "socket.io-client";

export default {
  name: "Server",
  data() {
    return {
      // 加载层信息
      loading: true,
      // 服务器信息
      server: {cpu: {}},

      redisData: {},
      mongoData: {},
    };
  },
  created() {
    const _this = this;
    _this.loading = true;
    _this.getRedisData();
    _this.getMongoData();

    this.socket = io("http://127.0.0.1:8080/server", {
      transports: ["websocket"],
    });
    this.socket.on("monitor_server", function (data) {
      console.log(data);
      if (_this.loading) {
        _this.loading = false;
        _this.server.cpu = data.cpu_info;
        _this.server.mem = data.memory_info;
      } else {
        _this.server.cpu = data.cpu_info;
        _this.server.mem = data.memory_info;
      }
    });
  },

  beforeDestroy() {
    this.socket.close();
  },

  methods: {
    getRedisData() {
      const _this = this;
      _this.listLoading = true;
      get_redis_data().then((response) => {
        console.log("response: ", response);
        _this.redisData = response.data;

        setTimeout(() => {
          _this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    getMongoData() {
      const _this = this;
      _this.listLoading = true;
      get_mongo_data().then((response) => {
        console.log("response: ", response);
        _this.mongoData = response.data;

        setTimeout(() => {
          _this.listLoading = false;
        }, 1.5 * 1000);
      });
    },
  },
};
</script>
