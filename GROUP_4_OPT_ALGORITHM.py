
import tkinter as tk
from tkinter import ttk, messagebox


class OPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OPT Page Replacement Algorithm")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e2530")

        self.bg = "#1e2530"
        self.panel = "#262e3d"
        self.border = "#3a4557"
        self.text_color = "#e6e9ef"
        self.muted = "#8b95a7"
        self.accent = "#4f8cff"
        self.hit_color = "#3fb27f"
        self.fault_color = "#e2574c"
        self.font_mono = ("Consolas", 10)
        self.font_mono_bold = ("Consolas", 10, "bold")

        self._build_input_panel()
        self._build_button_panel()
        self._build_table_panel()
        self._build_stats_panel()

    # ---------- UI construction ----------

    def _build_input_panel(self):
        frame = tk.Frame(self.root, bg=self.panel, bd=1, relief="solid",
                          highlightbackground=self.border, highlightthickness=1)
        frame.pack(fill="x", padx=16, pady=(16, 8))

        inner = tk.Frame(frame, bg=self.panel)
        inner.pack(fill="x", padx=12, pady=12)

        # Frame count input
        tk.Label(inner, text="NUMBER OF FRAMES", bg=self.panel, fg=self.muted,
                  font=("Consolas", 9)).grid(row=0, column=0, sticky="w")
        self.frame_entry = tk.Entry(inner, width=10, font=self.font_mono,
                                     bg="#1a212c", fg=self.text_color,
                                     insertbackground=self.text_color, relief="flat")
        self.frame_entry.insert(0, "3")
        self.frame_entry.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(4, 0))

        # Reference string input
        tk.Label(inner, text="REFERENCE STRING (space or comma separated)",
                  bg=self.panel, fg=self.muted, font=("Consolas", 9)).grid(
                  row=0, column=1, sticky="w")
        self.ref_entry = tk.Entry(inner, font=self.font_mono,
                                   bg="#1a212c", fg=self.text_color,
                                   insertbackground=self.text_color, relief="flat")
        self.ref_entry.grid(row=1, column=1, sticky="ew", pady=(4, 0))

        inner.columnconfigure(1, weight=1)

    def _build_button_panel(self):
        frame = tk.Frame(self.root, bg=self.bg)
        frame.pack(fill="x", padx=16, pady=(0, 8))

        self.run_btn = tk.Button(frame, text="Run", command=self.run_opt,
                                  bg=self.accent, fg="white", relief="flat",
                                  font=self.font_mono_bold, padx=18, pady=6,
                                  activebackground="#6ba0ff", cursor="hand2")
        self.run_btn.pack(side="left", padx=(0, 8))

        self.reset_btn = tk.Button(frame, text="Reset", command=self.reset,
                                    bg="#3a4557", fg=self.text_color, relief="flat",
                                    font=self.font_mono, padx=18, pady=6,
                                    activebackground="#4a5567", cursor="hand2")
        self.reset_btn.pack(side="left", padx=(0, 8))

        self.exit_btn = tk.Button(frame, text="Exit", command=self.exit_program,
                                   bg=self.fault_color, fg="white", relief="flat",
                                   font=self.font_mono, padx=18, pady=6,
                                   activebackground="#f06f64", cursor="hand2")
        self.exit_btn.pack(side="left")

    def _build_table_panel(self):
        outer = tk.Frame(self.root, bg=self.panel, highlightbackground=self.border,
                          highlightthickness=1)
        outer.pack(fill="both", expand=True, padx=16, pady=(0, 8))

        tk.Label(outer, text="RESULT TABLE", bg=self.panel, fg=self.muted,
                  font=("Consolas", 9)).pack(anchor="w", padx=12, pady=(10, 4))

        # Scrollable canvas holding the result table
        canvas_frame = tk.Frame(outer, bg=self.panel)
        canvas_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        self.table_canvas = tk.Canvas(canvas_frame, bg=self.panel,
                                       highlightthickness=0, height=260)
        h_scroll = tk.Scrollbar(canvas_frame, orient="horizontal",
                                 command=self.table_canvas.xview)
        v_scroll = tk.Scrollbar(canvas_frame, orient="vertical",
                                 command=self.table_canvas.yview)
        self.table_canvas.configure(xscrollcommand=h_scroll.set,
                                     yscrollcommand=v_scroll.set)

        self.table_inner = tk.Frame(self.table_canvas, bg=self.panel)
        self.table_canvas.create_window((0, 0), window=self.table_inner, anchor="nw")
        self.table_inner.bind(
            "<Configure>",
            lambda e: self.table_canvas.configure(scrollregion=self.table_canvas.bbox("all"))
        )

        self.table_canvas.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        canvas_frame.rowconfigure(0, weight=1)
        canvas_frame.columnconfigure(0, weight=1)

        self.empty_label = tk.Label(self.table_inner, text="No results yet. Enter data and press Run.",
                                     bg=self.panel, fg=self.muted, font=("Consolas", 10, "italic"))
        self.empty_label.pack(padx=4, pady=4)

    def _build_stats_panel(self):
        outer = tk.Frame(self.root, bg=self.panel, highlightbackground=self.border,
                          highlightthickness=1)
        outer.pack(fill="x", padx=16, pady=(0, 16))

        tk.Label(outer, text="STATISTICS", bg=self.panel, fg=self.muted,
                  font=("Consolas", 9)).pack(anchor="w", padx=12, pady=(10, 4))

        stats_frame = tk.Frame(outer, bg=self.panel)
        stats_frame.pack(fill="x", padx=12, pady=(0, 12))
        for i in range(4):
            stats_frame.columnconfigure(i, weight=1)

        self.hit_value = self._make_stat_box(stats_frame, 0, "HITS", self.hit_color)
        self.fault_value = self._make_stat_box(stats_frame, 1, "FAULTS", self.fault_color)
        self.hit_rate_value = self._make_stat_box(stats_frame, 2, "HIT RATE", self.text_color)
        self.fault_rate_value = self._make_stat_box(stats_frame, 3, "FAULT RATE", self.text_color)

    def _make_stat_box(self, parent, col, label, color):
        box = tk.Frame(parent, bg="#1a212c", highlightbackground=self.border,
                        highlightthickness=1)
        box.grid(row=0, column=col, sticky="ew", padx=6)

        value_label = tk.Label(box, text="-", bg="#1a212c", fg=color,
                                font=("Consolas", 18, "bold"))
        value_label.pack(pady=(10, 0))

        tk.Label(box, text=label, bg="#1a212c", fg=self.muted,
                  font=("Consolas", 8)).pack(pady=(0, 10))

        return value_label

    # ---------- OPT algorithm ----------

    def parse_ref_string(self, text):
        raw = text.replace(",", " ").split()
        return [int(x) for x in raw]

    def run_opt_algorithm(self, frame_count, refs):
        frames = [None] * frame_count
        steps = []
        hits = 0
        faults = 0

        for i, page in enumerate(refs):
            is_hit = page in frames

            if is_hit:
                hits += 1
            else:
                faults += 1
                if None in frames:
                    frames[frames.index(None)] = page
                else:
                    farthest_index = -1
                    farthest_pos = -1
                    future = refs[i + 1:]
                    for f_idx, f_page in enumerate(frames):
                        if f_page not in future:
                            farthest_index = f_idx
                            break
                        next_use = future.index(f_page)
                        if next_use > farthest_pos:
                            farthest_pos = next_use
                            farthest_index = f_idx
                    frames[farthest_index] = page

            steps.append({"page": page, "frames": list(frames), "hit": is_hit})

        return steps, hits, faults

    # ---------- Event handlers ----------

    def run_opt(self):
        frame_text = self.frame_entry.get().strip()
        ref_text = self.ref_entry.get().strip()

        if not frame_text.isdigit() or int(frame_text) < 1:
            messagebox.showerror("Invalid input", "Please enter a valid number of frames (1 or more).")
            return

        if not ref_text:
            messagebox.showerror("Invalid input", "Please enter a reference string.")
            return

        try:
            refs = self.parse_ref_string(ref_text)
        except ValueError:
            messagebox.showerror("Invalid input", "Reference string must contain only numbers.")
            return

        frame_count = int(frame_text)
        steps, hits, faults = self.run_opt_algorithm(frame_count, refs)

        self.render_table(steps, frame_count)
        self.render_stats(hits, faults)

    def render_table(self, steps, frame_count):
        for widget in self.table_inner.winfo_children():
            widget.destroy()

        def cell(r, c, value, bg="#1a212c", fg=None, bold=False, anchor="center", width=6):
            fg = fg or self.text_color
            font = self.font_mono_bold if bold else self.font_mono
            lbl = tk.Label(self.table_inner, text=value, bg=bg, fg=fg, font=font,
                            width=width, anchor=anchor, relief="solid", bd=1,
                            highlightbackground=self.border)
            lbl.grid(row=r, column=c, sticky="nsew")

        # Header row: reference values
        cell(0, 0, "Reference", bg="#1a212c", fg=self.muted, bold=True, anchor="w", width=12)
        for i, step in enumerate(steps):
            cell(0, i + 1, str(step["page"]), bg="#1a212c", fg=self.muted, bold=True)

        # Frame rows
        for f in range(frame_count):
            cell(f + 1, 0, f"Frame {f + 1}", bg=self.panel, fg=self.muted, anchor="w", width=12)
            for i, step in enumerate(steps):
                val = step["frames"][f]
                display = "" if val is None else str(val)
                cell(f + 1, i + 1, display, bg=self.panel)

        # Status row
        status_row = frame_count + 1
        cell(status_row, 0, "Status", bg=self.panel, fg=self.muted, anchor="w", width=12)
        for i, step in enumerate(steps):
            if step["hit"]:
                cell(status_row, i + 1, "Hit", bg=self.panel, fg=self.hit_color, bold=True)
            else:
                cell(status_row, i + 1, "Fault", bg=self.panel, fg=self.fault_color, bold=True)

    def render_stats(self, hits, faults):
        total = hits + faults
        self.hit_value.config(text=str(hits))
        self.fault_value.config(text=str(faults))
        if total > 0:
            self.hit_rate_value.config(text=f"{(hits / total) * 100:.1f}%")
            self.fault_rate_value.config(text=f"{(faults / total) * 100:.1f}%")
        else:
            self.hit_rate_value.config(text="-")
            self.fault_rate_value.config(text="-")

    def reset(self):
        self.frame_entry.delete(0, tk.END)
        self.frame_entry.insert(0, "3")
        self.ref_entry.delete(0, tk.END)

        for widget in self.table_inner.winfo_children():
            widget.destroy()
        self.empty_label = tk.Label(self.table_inner, text="No results yet. Enter data and press Run.",
                                     bg=self.panel, fg=self.muted, font=("Consolas", 10, "italic"))
        self.empty_label.pack(padx=4, pady=4)

        self.hit_value.config(text="-")
        self.fault_value.config(text="-")
        self.hit_rate_value.config(text="-")
        self.fault_rate_value.config(text="-")

    def exit_program(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = OPTApp(root)
    root.mainloop()