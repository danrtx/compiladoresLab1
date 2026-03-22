import sys
import os
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser.DevOpsDSLVisitor import DevOpsDSLVisitor

class Interpreter(DevOpsDSLVisitor):
    def __init__(self, executor):
        self.executor = executor

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitNodeCommand(self, ctx):
        node = ctx.ID().getText()
        script = ctx.STRING().getText().replace('"', '')
        self.executor.run_on_node(node, script)

    def visitGroupCommand(self, ctx):
        group = ctx.ID().getText()
        self.executor.update_group(group)

    def visitDeployCommand(self, ctx):
        app_name = ctx.ID(0).getText()
        group_name = ctx.ID(1).getText()
        self.executor.deploy(app_name, group_name)

    def visitRule(self, ctx):
        condition_result = self.visit(ctx.condition())
        if condition_result:
            self.visit(ctx.action())

    def visitCondition(self, ctx):
        node_name = ctx.ID(0).getText()
        sensor_type = ctx.ID(1).getText()
        comparator = self.visit(ctx.comparator())
        value = float(ctx.NUMBER().getText())

        data = self.executor.get_sensor_data(node_name)
        current_val = data.get(sensor_type, 0)

        if comparator == '>': return current_val > value
        if comparator == '<': return current_val < value
        if comparator == '==': return current_val == value
        if comparator == '!=': return current_val != value
        if comparator == '>=': return current_val >= value
        if comparator == '<=': return current_val <= value
        return False

    def visitComparator(self, ctx):
        return ctx.getText()

    def visitAction(self, ctx):
        if ctx.STRING():
            node = ctx.ID().getText()
            script = ctx.STRING().getText().replace('"', '')
            self.executor.run_on_node(node, script)
        else:
            func = ctx.ID().getText()
            print(f"[EVENTO] Ejecutando acción interna: {func}()")

    def visitParallelBlock(self, ctx):
        print(f"[INFO] Iniciando bloque paralelo...")
        threads = []
        statements = ctx.statement()
        for statement in statements:
            t = threading.Thread(target=self.visit, args=(statement,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        print(f"[INFO] Bloque paralelo completado.\n")
    
