<template>
  <div class="app-container">
    <el-row :gutter="20">
      <el-col
        :xs="24"
        :sm="24"
        :md="10"
        :lg="8"
        :xl="8"
        style="margin-bottom: 10px"
      >
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>supervisor 节点管理</span>
            <el-button type="success" size="mini" @click="handleNodeCreate"
            >新增
            </el-button
            >
          </div>

          <el-table
            :key="tableKey"
            v-loading="listLoading"
            :data="nodeList"
            fit
            highlight-current-row
            @row-click="nodeProcessList"
            style="width: 100%"
          >
            <el-table-column align="center" label="node" width="150">
              <template slot-scope="{ row }">
                <span>{{ row.general.name }}</span>
              </template>
            </el-table-column>
            <el-table-column width="90px" align="center" label="connected">
              <template slot-scope="{ row }">
                <el-row>
                  <el-button
                    v-if="row.general.connected"
                    type="success"
                    icon="el-icon-check"
                    circle
                  ></el-button>
                  <el-button
                    v-else
                    type="info"
                    icon="el-icon-close"
                    circle
                  ></el-button>
                </el-row>
              </template>
            </el-table-column>

            <!--            <el-table-column width="110px" align="center" label="environment">-->
            <!--              <template slot-scope="{ row }">-->
            <!--                <span>{{ row.general.environment }}</span>-->
            <!--              </template>-->
            <!--            </el-table-column>-->

            <el-table-column label="操作" align="center" width="">
              <template slot-scope="{ row, $index }">
                <div>
                  <el-button
                    type="primary"
                    icon="el-icon-search"
                    size="mini"
                    @click.stop="() => handleNodeUpdate(row)"
                  >编辑
                  </el-button
                  >
                  <el-button
                    type="danger"
                    icon="el-icon-delete"
                    size="mini"
                    @click.stop="() => handleNodeDelete(row)"
                  >删除
                  </el-button
                  >
                </div>
              </template>
            </el-table-column>
          </el-table>

          <pagination
            v-show="node_total > 0"
            :total="node_total"
            :page.sync="listQuery.page"
            :limit.sync="listQuery.limit"
            @pagination="getList"
          />
        </el-card>
      </el-col>

      <!-- 详情列表 -->
      <el-col :xs="24" :sm="24" :md="14" :lg="16" :xl="16">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>supervisor 进程管理</span>
          </div>
          <el-form :inline="true" label-position="right">
            <el-form-item size="small">
              <el-button type="success" @click="startAllProcess(row)">START ALL</el-button>
            </el-form-item>
            <el-form-item size="small">
              <el-button type="warning" @click="stopAllProcess(row)">STOP ALL</el-button>
            </el-form-item>
            <el-form-item size="small">
              <el-button type="primary" @click="restartAllProcess(row)">RESTART ALL</el-button>
            </el-form-item>
          </el-form>

          <el-table
            :key="tableKey"
            v-loading="listLoading"
            :data="processList"
            aria-setsize
            fit
            highlight-current-row
            style="width: 100%"
          >
            <el-table-column align="center" label="node" width="130px">
              <template slot-scope="{ row }">
                <span>{{ general.name }}</span>
              </template>
            </el-table-column>

            <!-- <el-table-column align="center" label="pid" width="90">
              <template slot-scope="{ row }">
                <span>{{ row.pid }}</span>
              </template>
            </el-table-column> -->

            <el-table-column width="120px" align="center" label="name">
              <template slot-scope="{ row }">
                <span>{{ row.name }}</span>
              </template>
            </el-table-column>

            <el-table-column width="240px" align="center" label="description">
              <template slot-scope="{ row }">
                <span>{{ row.description }}</span>
              </template>
            </el-table-column>

            <el-table-column label="statename" width="140px" align="center">
              <template slot-scope="{ row }">
                <div>
                  <el-button
                    v-if="row.statename == 'RUNNING'"
                    type="success"
                    size="mini"
                    plain
                  >运行中
                  </el-button
                  >
                  <el-button v-else type="danger" plain size="mini"
                  >已停止
                  </el-button>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="操作" align="center" fixed="right" width="">
              <template slot-scope="{ row, $index }">
                <div>
                  <el-button
                    type="success"
                    size="mini"
                    @click="startProcess(row)"
                  >Start
                  </el-button
                  >

                  <el-button
                    type="warning"
                    size="mini"
                    @click="stopProcess(row)"
                  >Stop
                  </el-button
                  >

                  <el-button
                    type="primary"
                    size="mini"
                    @click="restartProcess(row)"
                  >Restart
                  </el-button
                  >
                  <el-button
                    type="info"
                    size="mini"
                    @click="handleStdoutLog(row)"
                  >StdoutLog
                  </el-button
                  >
                  <el-button type="danger" size="mini">StderrLog</el-button>
                </div>
              </template>
            </el-table-column>
          </el-table>

          <pagination
            v-show="process_total > 0"
            :total="process_total"
            :page.sync="listQuery.page"
            :limit.sync="listQuery.limit"
            @pagination="getList"
          />
        </el-card>
      </el-col>
    </el-row>

    <el-dialog
      :title="nodeDialogStatus"
      :visible.sync="createNodeVisible"
      width="40%"
    >
      <el-form rules="rules" :model="temp" ref="dataForm" label-width="100px">
        <el-form-item prop="" label="节点名称">
          <el-input v-model="temp.name" placeholder="节点名称"></el-input>
        </el-form-item>

        <el-form-item prop="" label="服务器地址">
          <el-input v-model="temp.host" placeholder="服务器地址"></el-input>
        </el-form-item>

        <el-form-item prop="" label="服务器端口">
          <el-input v-model="temp.port" placeholder="服务器端口"></el-input>
        </el-form-item>

        <el-form-item prop="" label="用户名">
          <el-input v-model="temp.user" placeholder="用户名"></el-input>
        </el-form-item>

        <el-form-item prop="" label="密码">
          <el-input v-model="temp.pwd" placeholder="密码"></el-input>
        </el-form-item>

        <el-form-item prop="" label="所属环境">
          <el-select placeholder="请选择">
            <el-option label="A组" value="A组"></el-option>
            <el-option label="B组" value="B组"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="" label="描述">
          <el-input v-model="temp.pwd" placeholder="描述"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer">
        <el-button @click="createNodeVisible = false">取 消</el-button>
        <el-button
          type="primary"
          @click="
            nodeDialogStatus === 'create' ? createNodeData() : updateNodeData()
          "
        >
          确认
        </el-button>
      </span>
    </el-dialog>

    <el-drawer
      title="Process Log"
      :visible.sync="drawer"
      :direction="direction"
      size="38%"
    >
      <div style="margin-left: 20px">
        <el-button type="primary" plain>{{
            processLogItem.generalName
          }}
        </el-button>
        <el-button type="success" plain>{{
            processLogItem.processName
          }}
        </el-button>
        <!-- <span>青春是一个短暂的美梦, 当你醒来时, 它早已消失无踪</span> -->
        <el-divider></el-divider>
        <div
          v-for="(item, index) in processLogItem.processLogList"
          :key="index"
        >
          <span>{{ item }}</span>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
import {
  get_nodes,
  get_node,
  stop_process,
  start_process,
  restart_process,
  read_process_log,
} from "@/api/supervisor";
import waves from "@/directive/waves"; // waves directive
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

export default {
  name: "Nodes",
  components: {Pagination},
  directives: {waves},
  data() {
    return {
      tableKey: 0,
      nodeList: null,
      processList: null,
      general: null,
      processLogItem: {
        processLogList: [],
        processName: null,
        generalName: null,
      },
      node_total: 0,
      process_total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        project: "",
        status: "",
      },

      createNodeVisible: false,
      logVisible: false,
      nodeVisible: false,
      logDialogStatus: "",
      nodeDialogStatus: "",
      downloadLoading: false,
      drawer: false,
      direction: "rtl",

      temp: {
        name: "",
        host: "",
        port: "",
        user: "",
        pwd: "",
        update_time: "",
      },
    };
  },
  created() {
    this.getList();
  },
  methods: {
    getList() {
      this.listLoading = true;
      console.log("listQuery: ", this.listQuery);
      get_nodes().then((response) => {
        console.log("response: ", response);
        this.nodeList = response.data.items;
        this.node_total = response.data.total || 2;
        setTimeout(() => {
          this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    resetTemp() {
      this.temp = {
        name: "",
        host: "",
        port: "",
        user: "",
        pwd: "",
        update_time: this.dayjs().format("YYYY-MM-DD HH:mm:ss"),
      };
    },

    // 新增节点
    handleNodeCreate() {
      this.resetTemp();
      this.nodeDialogStatus = "create";
      this.createNodeVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },

    createNodeData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          // create_xhs_comment(this.temp).then(() => {
          this.createNodeVisible = false;
          this.$notify({
            title: "Success",
            message: "未开放的功能",
            type: "success",
            duration: 2000,
          });
          // });
        }
      });
    },

    // 更新节点
    handleNodeUpdate(row) {
      this.temp = Object.assign({}, row.general); // copy obj
      console.log("temp: ", this.temp);
      this.nodeDialogStatus = "update";
      this.createNodeVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },

    updateNodeData() {
      this.$refs["dataForm"].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp);
          // update_xhs_comment(tempData).then(() => {
          this.createNodeVisible = false;
          this.$notify({
            title: "Success",
            message: "未开放的功能",
            type: "success",
            duration: 2000,
          });
          // });
        }
      });
    },

    // 删除节点
    handleNodeDelete(row, index) {
      this.$notify({
        title: "删除节点",
        message: "请联系管理员删除",
        type: "error",
        duration: 2000,
      });
    },

    handleStdoutLog(row) {
      // this.logDialogStatus = "stdout";
      // this.logVisible = true;
      this.drawer = true;
      this.getProcessLog(row);
    },

    getProcessLog(row) {
      // this.listLoading = true;
      console.log("listQuery: ", this.listQuery);
      read_process_log(this.general.name, row.name).then((response) => {
        this.processLogItem.processLogList = response.data.log.stdout;
        this.processLogItem.generalName = this.general.name;
        this.processLogItem.processName = row.name;
        setTimeout(() => {
          // this.listLoading = false;
        }, 3 * 1000);
      });
    },

    nodeProcessList(row) {
      // console.log(row);
      // this.listLoading = true;
      get_node(row.general.name).then((response) => {
        console.log("response: ", response);
        this.processList = response.data.items.processes;
        this.general = response.data.items.general;
        this.process_total = response.data.total || 2;
        setTimeout(() => {
          // this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    nodeProcessList_(name) {
      // this.listLoading = true;
      get_node(name).then((response) => {
        console.log("response: ", response);
        this.processList = response.data.items.processes;
        this.general = response.data.items.general;
        this.process_total = response.data.total || 2;
        setTimeout(() => {
          // this.listLoading = false;
        }, 1.5 * 1000);
      });
    },

    startProcess(row) {
      this.$confirm("确定要开启该 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          start_process(this.general.name, row.name).then((res) => {
            if (res.code === 20000) {
              this.$message.success(row.name + "已启动");
              this.nodeProcessList_(this.general.name);
            }
          });
        })
        .catch(() => {
        });
    },

    stopProcess(row) {
      this.$confirm("确定要停止该 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          stop_process(this.general.name, row.name).then((res) => {
            if (res.code === 20000) {
              this.$message.success(row.name + "已停止");
              this.nodeProcessList_(this.general.name);
            }
          });
        })
        .catch(() => {
        });
    },

    restartProcess(row) {
      this.$confirm("确定要重启该 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          restart_process(this.general.name, row.name).then((res) => {
            if (res.code === 20000) {
              this.$message.success(row.name + "重启成功");
              this.nodeProcessList_(this.general.name);
            }
          });
        })
        .catch(() => {
        });
    },

    startAllProcess(row) {
      this.$confirm("确定要开启所有 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          // _process(this.general.name, row.name).then((res) => {
          //   if (res.code === 20000) {
          //     this.$message.success(row.name + "已启动");
          //     this.nodeProcessList_(this.general.name);
          //   }
          // });
          this.$notify({
            title: "Success",
            message: "未开放的功能",
            type: "success",
            duration: 2000,
          });
        })
        .catch(() => {
        });
    },
    stopAllProcess(row) {
      this.$confirm("确定要暂停所有 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          // _process(this.general.name, row.name).then((res) => {
          //   if (res.code === 20000) {
          //     this.$message.success(row.name + "已启动");
          //     this.nodeProcessList_(this.general.name);
          //   }
          // });
          this.$notify({
            title: "Success",
            message: "未开放的功能",
            type: "success",
            duration: 2000,
          });
        })
        .catch(() => {
        });
    },

    restartAllProcess(row) {
      this.$confirm("确定要重启所有 Process 吗?", "提示", {
        type: "warning",
      })
        .then(() => {
          // _process(this.general.name, row.name).then((res) => {
          //   if (res.code === 20000) {
          //     this.$message.success(row.name + "已启动");
          //     this.nodeProcessList_(this.general.name);
          //   }
          // });
          this.$notify({
            title: "Success",
            message: "未开放的功能",
            type: "success",
            duration: 2000,
          });
        })
        .catch(() => {
        });
    },
  },
};
</script>
