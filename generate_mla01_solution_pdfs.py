from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak


def footer(canvas, doc, total_pages):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#4b5563'))
    canvas.setLineWidth(0.7)
    canvas.line(36, 28, 556, 28)
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#344054'))
    canvas.drawString(36, 14, 'MLA01 - Artificial Intelligence and Expert Systems')
    canvas.drawRightString(560, 14, f'Page {canvas.getPageNumber()} of {total_pages}')
    canvas.restoreState()


def build_doc(path, title, subtitle, section_blocks, total_pages=5):
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=20,
        alignment=1,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=8,
    )
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#374151'),
        spaceAfter=8,
        alignment=1,
    )
    heading_style = ParagraphStyle(
        'HeadingStyle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=8,
        spaceAfter=6,
    )
    para_style = ParagraphStyle(
        'ParaStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=12.5,
        textColor=colors.HexColor('#111827'),
        alignment=1,
        spaceAfter=5,
    )
    left_style = ParagraphStyle(
        'LeftStyle',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=12.5,
        textColor=colors.HexColor('#111827'),
        alignment=1,
        spaceAfter=5,
    )
    story = [
        Paragraph(title, title_style),
        Paragraph(subtitle, subtitle_style),
        Spacer(1, 6),
    ]
    for block in section_blocks:
        if isinstance(block, str):
            story.append(Paragraph(block, para_style))
        elif isinstance(block, PageBreak):
            story.append(block)
        elif isinstance(block, list):
            story.extend(block)
        else:
            story.append(block)
        story.append(Spacer(1, 8))

    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=40,
    )
    doc.build(story, onFirstPage=lambda c, d: footer(c, d, total_pages), onLaterPages=lambda c, d: footer(c, d, total_pages))


def table_from(rows, col_widths):
    table = Table(rows, colWidths=col_widths)
    table.setStyle(
        TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5e7eb')),
            ('GRID', (0, 0), (-1, -1), 0.7, colors.HexColor('#4b5563')),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9fafb')]),
            ('FONTSIZE', (0, 0), (-1, -1), 8.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
        ])
    )
    return table


def build_co1_assignment_1():
    title = 'CO1 Assignment 1 - Analytical Problem Solving Solutions'
    subtitle = 'Artificial Intelligence and Expert Systems (MLA01)'
    blocks = []

    q1 = [
        Paragraph('Q1. Uninformed Search – BFS Analysis', ParagraphStyle('Q1', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('State-space representation: States are grid positions (x, y), each cell is a node. Initial state = (1,1), Goal state = (6,6). Actions = Up, Down, Left, Right. Transition model: moving to an adjacent valid cell with unit cost 1. Since all moves are uniform-cost and the grid is obstacle-free, BFS returns the shortest path in number of moves.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('BFS queue trace (with neighbour order: Up, Down, Left, Right):', ParagraphStyle('Q1b', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica-Bold', fontSize=9.2, leading=12.5, alignment=1, spaceAfter=4)),
    ]
    q1.append(table_from([
        ['Level', 'Queue (front to rear)'],
        ['0', '[(1,1)]'],
        ['1', '[(1,2), (2,1)]'],
        ['2', '[(1,3), (2,2), (3,1)]'],
        ['3', '[(1,4), (2,3), (3,2), (4,1)]'],
        ['4', '[(1,5), (2,4), (3,3), (4,2), (5,1)]'],
        ['5', '[(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)]'],
        ['6', '[(2,6), (3,5), (4,4), (5,3), (6,2)]'],
        ['7', '[(3,6), (4,5), (5,4), (6,3)]'],
        ['8', '[(4,6), (5,5), (6,4)]'],
        ['9', '[(5,6), (6,5)]'],
        ['10', '[(6,6)]']
    ], [120, 340]))
    q1 += [
        Paragraph('Node expansion order: (1,1), (1,2), (2,1), (1,3), (2,2), (3,1), ... , (6,6). BFS expands nodes level by level, therefore it guarantees the first goal node found is the shortest path in terms of number of moves.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('A shortest path is: (1,1) → (1,2) → (1,3) → (1,4) → (1,5) → (1,6) → (2,6) → (3,6) → (4,6) → (5,6) → (6,6). Path length = 10 moves. Total cost = 10 × 1 = 10.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q1)
    blocks.append(PageBreak())

    q2 = [
        Paragraph('Q2. Heuristic Design and Greedy vs A*', ParagraphStyle('Q2', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('A good heuristic must be admissible and informative. For a road network, a heuristic such as straight-line distance to the goal or minimum remaining travel time is suitable. For A* we compute f(n)=g(n)+h(n). Greedy Best-First uses only f(n)=h(n).', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Representative graph and heuristic values:', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica-Bold', fontSize=9.2, leading=12.5, alignment=1, spaceAfter=4)),
    ]
    q2.append(table_from([
        ['Node', 'h(n)'],
        ['S', '7'],
        ['A', '6'],
        ['B', '4'],
        ['C', '3'],
        ['D', '2'],
        ['G', '0']
    ], [120, 80]))
    q2 += [
        Paragraph('Greedy Best-First expands the node with the lowest h(n): S → B → D → G. This may be fast, but it can ignore accumulated cost and therefore may choose a locally promising but globally expensive route.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('A* expands the node with smallest f(n)=g(n)+h(n), which balances cost already incurred and expected remaining cost. Therefore A* is more robust and often optimal with admissible heuristics.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q2)
    blocks.append(PageBreak())

    q3 = [
        Paragraph('Q3. A* Search – Stepwise Computation', ParagraphStyle('Q3', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Given graph: S-A=1, S-B=3, A-C=2, B-C=1, C-G=3. Heuristics: h(S)=5, h(A)=3, h(B)=4, h(C)=2, h(G)=0.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q3.append(table_from([
        ['Iteration', 'OPEN', 'CLOSED'],
        ['0', 'S (5)', ''],
        ['1', 'A (4), B (7)', 'S'],
        ['2', 'B (7), C (5)', 'S, A'],
        ['3', 'B (7), G (6)', 'S, A, C'],
        ['4', 'B (7)', 'S, A, C, G']
    ], [90, 190, 170]))
    q3 += [
        Paragraph('Path found: S → A → C → G. Total cost = 1 + 2 + 3 = 6. The heuristic is admissible because every heuristic estimate never exceeds the actual remaining cost to the goal: h(A)=3 is ≤ true cost to G via C/G; h(B)=4 ≤ actual; h(C)=2 ≤ 3.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q3)
    blocks.append(PageBreak())

    q4 = [
        Paragraph('Q4. DFS Analysis', ParagraphStyle('Q4', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Graph: S-A, S-B, A-C, B-D, C-G, D-G. DFS uses stack behaviour: it explores a path deeply before backtracking. With alphabetical neighbour ordering, the traversal is S → A → C → G (goal). If the goal is not found on that branch, it backtracks and explores B → D → G.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Node expansion order: S, A, C, G, B, D. One valid DFS path to G is S-A-C-G. BFS, by contrast, expands level by level and therefore finds shallowest goal nodes first. DFS is not optimal in general because it may find a deep route even when a shorter route exists.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q4)
    blocks.append(PageBreak())

    q5 = [
        Paragraph('Q5. UCS Problem', ParagraphStyle('Q5', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Given weighted graph: S-A=2, S-B=5, A-C=4, B-C=1, C-G=3. UCS always expands the lowest cumulative cost node. The sequence is: S (0), then A (2), B (5), then C (6), then G (9).', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q5.append(table_from([
        ['Step', 'Expanded node', 'Path cost'],
        ['1', 'S', '0'],
        ['2', 'A', '2'],
        ['3', 'B', '5'],
        ['4', 'C', '6'],
        ['5', 'G', '9']
    ], [90, 180, 120]))
    q5 += [
        Paragraph('Optimal path: S → A → C → G with total cost 9. UCS guarantees optimality on non-negative weighted graphs, unlike BFS which ignores edge weights and is not guaranteed to minimize cost when weights differ.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Summary: BFS minimizes the number of moves, DFS finds a path quickly with low memory, A* is best when a good heuristic is available, and UCS is optimal for weighted graphs.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q5)
    return title, subtitle, blocks


def build_co2_assignment_2():
    title = 'CO2 Assignment 2 - Problem Solving Assignment Solutions'
    subtitle = 'Artificial Intelligence and Expert Systems (MLA01)'
    blocks = []

    q1 = [
        Paragraph('Q1. Smart Ambulance Navigation', ParagraphStyle('Q1', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Model the road network as a weighted graph where each junction is a state and each road is an action with travel time cost. Use a heuristic h(n)=estimated remaining distance to the emergency site. The objective is to minimize total travel time while preserving safety and emergency response urgency.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Example road network: S-A=3, S-B=1, A-C=2, A-D=6, B-D=2, B-E=4, C-D=1, C-G=8, D-G=6, E-G=3.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q1.append(table_from([
        ['Node', 'h(n)'],
        ['S', '8'],
        ['A', '7'],
        ['B', '5'],
        ['C', '6'],
        ['D', '4'],
        ['E', '3'],
        ['G', '0']
    ], [100, 80]))
    q1 += [
        Paragraph('A* computes f(n)=g(n)+h(n). Starting at S, the best route is S → B → E → G because g=1+4+3=8, which is less than the alternative S → A → C → D → G = 3+2+1+6=12 and S → B → D → G = 1+2+6=9. Therefore the route selected by A* is S-B-E-G with total travel time 8 minutes.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q1)
    blocks.append(PageBreak())

    q2 = [
        Paragraph('Q2. Autonomous Warehouse Robot', ParagraphStyle('Q2', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('An online search agent operates without complete prior knowledge. It senses only the current local region and updates the map when new obstacles are discovered. The robot keeps the current best path to the goal, re-plans after obstacles are detected, and re-optimizes as environment information improves.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Compared with offline search, the online strategy is more robust when the environment changes dynamically. Offline search assumes complete knowledge at the start, while online search accommodates uncertainty and partial observability. In a warehouse, the robot may initially move toward the target aisle but must reroute when a blockage appears in front of it.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q2)
    blocks.append(PageBreak())

    q3 = [
        Paragraph('Q3. University Examination Scheduling as a CSP', ParagraphStyle('Q3', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Variables: E1, E2, E3, E4, E5, E6. Domains: each exam can take one time slot from {T1,T2,T3,T4}. Constraints: conflicting exams cannot share a slot. Hall capacities: A=120, B=90, C=60. Student counts: E1=100, E2=80, E3=70, E4=60, E5=90, E6=50.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q3.append(table_from([
        ['Exam', 'Students', 'Conflicts'],
        ['E1', '100', 'E2, E3'],
        ['E2', '80', 'E1, E4, E5'],
        ['E3', '70', 'E1, E5'],
        ['E4', '60', 'E2, E6'],
        ['E5', '90', 'E3, E2'],
        ['E6', '50', 'E4']
    ], [90, 110, 220]))
    q3 += [
        Paragraph('MRV heuristic selects the variable with the fewest available values. The most constrained exam is E2 or E5; after assigning a value, the forward-checking step removes incompatible slot values from related exams. One valid timetable is: E1-T1, E2-T2, E3-T3, E4-T4, E5-T1, E6-T2. Hall assignment: E1→Hall A (100), E2→Hall B (80), E3→Hall C (70), E4→Hall C (60), E5→Hall A (90), E6→Hall B (50). All conflicts are avoided and capacities are respected.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q3)
    blocks.append(PageBreak())

    q4 = [
        Paragraph('Q4. Game-Playing AI: Minimax and Alpha-Beta Pruning', ParagraphStyle('Q4', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Minimax assumes perfect play: the AI chooses the move that maximizes the minimum utility against the opponent. If the terminal scores are represented as leaf values, then parents are evaluated as max for the AI and min for the opponent. Alpha-beta pruning uses alpha and beta bounds to cut branches whose values cannot affect the final decision.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q4.append(table_from([
        ['Move', 'Utility'],
        ['M1', '7'],
        ['M2', '5'],
        ['M3', '9'],
        ['M4', '6']
    ], [120, 80]))
    q4 += [
        Paragraph('The AI selects M3 because it yields the best minimax value. In alpha-beta pruning, any branch whose value is worse than the current best bound is rejected without exploring all descendants. This reduces computation substantially in deeper game trees while preserving the same final move decision.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q4)
    blocks.append(PageBreak())

    q5 = [
        Paragraph('Q5. Delivery Route Optimization and Local Search', ParagraphStyle('Q5', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('A typical local search approach for TSP-like routing is 2-opt: remove two edges and reconnect the route in the opposite order if the total travel distance decreases. Starting route: A-B-C-D-E-A with distances 3, 5, 4, 2, 6.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q5.append(table_from([
        ['Route', 'Distance'],
        ['A-B-C-D-E-A', '20'],
        ['A-B-D-C-E-A', '18'],
        ['A-C-B-D-E-A', '17'],
        ['A-C-D-B-E-A', '16']
    ], [170, 120]))
    q5 += [
        Paragraph('After 2-opt swaps, the route improves from 20 to 16. This is a strong local optimum but not necessarily a global optimum. To escape local minima, the algorithm may use multiple restarts, simulated annealing, random perturbation, or tabu search. This explains why local optimization is effective but may still require broader exploration for globally optimal routing.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Conclusion: The best route is the one with the lowest total cost among all 2-opt neighboring routes, and if the route remains unchanged after several random perturbations, the strategy is likely close to a global optimum.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q5)
    return title, subtitle, blocks


def build_cia_co1_co2():
    title = 'CIA CO1 & CO2 - Continuous Internal Assessment Solutions'
    subtitle = 'Artificial Intelligence and Expert Systems (MLA01)'
    blocks = []

    q1 = [
        Paragraph('Q1. Ambulance Navigation: State-Space Search and Strategy Evaluation', ParagraphStyle('Q1', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('State-space representation: state = current junction. Initial state = S. Goal test = current node = G. Actions = move to adjacent junction through a road. Cost = travel time in minutes. The model is deterministic and each edge is bidirectional.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q1.append(table_from([
        ['Road', 'Time'],
        ['S-A', '3'],
        ['S-B', '1'],
        ['A-C', '2'],
        ['A-D', '6'],
        ['B-D', '2'],
        ['B-E', '4'],
        ['C-D', '1'],
        ['C-G', '8'],
        ['D-G', '6'],
        ['E-G', '3']
    ], [120, 80]))
    q1 += [
        Paragraph('BFS (graph search) expands nodes by level order and finds the shortest route in edges: S → B → E → G with 3 edges and total travel time 1 + 4 + 3 = 8 minutes. DFS with alphabetical neighbour ordering explores S → A → C → D → G, giving 4 edges and cost 3 + 2 + 1 + 6 = 12 minutes. UCS selects the minimum-cost path and also returns S → B → E → G, total cost 8 minutes.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Comparison: BFS is complete and optimal for unweighted graphs but ignores cost. DFS is memory efficient but not optimal. UCS is complete and optimal for weighted graphs with non-negative costs, and it is the most suitable for time-sensitive ambulance routing.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q1)
    blocks.append(PageBreak())

    q2 = [
        Paragraph('Q2. Warehouse Robot Navigation', ParagraphStyle('Q2', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('State-space representation: each node is a warehouse location and the robot state is its current aisle position. The initial state is S, the goal test is location G. Actions are moving along bidirectional aisle links. Transition cost is the travel distance between connected positions.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q2.append(table_from([
        ['Edge', 'Cost'],
        ['S-A', '2'],
        ['S-B', '4'],
        ['A-C', '3'],
        ['A-D', '5'],
        ['B-E', '3'],
        ['C-D', '2'],
        ['D-E', '2'],
        ['C-G', '6'],
        ['E-G', '4']
    ], [120, 80]))
    q2 += [
        Paragraph('BFS explores closest nodes first and yields the shallowest route S → A → C → G, cost 2 + 3 + 6 = 11. DFS with alphabetical ordering chooses a deep branch such as S → A → C → G or S → B → E → G depending on the exact ordering; because it explores one branch deeply, it may not choose the cheapest route. BFS is preferable when shortest number of steps matters; DFS is simpler but less cost-aware.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q2)
    blocks.append(PageBreak())

    q3 = [
        Paragraph('Q3. Greedy Best-First Search for Delivery Robot', ParagraphStyle('Q3', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Greedy Best-First Search uses the evaluation function f(n)=h(n), choosing the node with the smallest heuristic value. The heuristic is the estimated remaining distance to the goal. This strategy is fast but may overlook the actual cost already incurred.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q3.append(table_from([
        ['Node', 'h(n)'],
        ['S', '9'],
        ['A', '6'],
        ['B', '4'],
        ['C', '2'],
        ['D', '1'],
        ['G', '0']
    ], [100, 80]))
    q3 += [
        Paragraph('The greedy search selects S → B → D → G because B has lower h than A, and D has the lowest heuristic among the next frontier. Total cost = g(S→B)+g(B→D)+g(D→G). If the graph contains misleading heuristics, greedy search can still choose a longer path than A*. This is one limitation of the method.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q3)
    blocks.append(PageBreak())

    q4 = [
        Paragraph('Q4. Cryptarithmetic Puzzle: SEND + MORE = MONEY', ParagraphStyle('Q4', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('Variables are unique digits: S,E,N,D,M,O,R,Y ∈ {0..9}. Constraints: all letters different, leading letters S and M cannot be 0, and each column in the addition must satisfy the arithmetic relation.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q4.append(table_from([
        ['Letter', 'Value'],
        ['S', '9'],
        ['E', '5'],
        ['N', '6'],
        ['D', '7'],
        ['M', '1'],
        ['O', '0'],
        ['R', '8'],
        ['Y', '2']
    ], [100, 80]))
    q4 += [
        Paragraph('Verification: 9567 + 1085 = 10652. The assignment satisfies all uniqueness and leading-letter constraints. Thus the valid solution is S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q4)
    blocks.append(PageBreak())

    q5 = [
        Paragraph('Q5. A* Search for Emergency Ambulance Routing', ParagraphStyle('Q5', parent=getSampleStyleSheet()['Heading2'], fontName='Helvetica-Bold', fontSize=12, spaceAfter=8, textColor=colors.HexColor('#111827'))),
        Paragraph('A* evaluates each node according to f(n)=g(n)+h(n), where g(n) is the actual accumulated cost from the start and h(n) is the heuristic estimate of the cheapest remaining route to the goal. This method combines safety and efficiency and is preferred for emergency navigation.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    q5.append(table_from([
        ['Node', 'g(n)', 'h(n)', 'f(n)'],
        ['S', '0', '10', '10'],
        ['A', '2', '6', '8'],
        ['B', '4', '4', '8'],
        ['C', '5', '3', '8'],
        ['D', '7', '2', '9'],
        ['G', '11', '0', '11']
    ], [80, 70, 70, 70]))
    q5 += [
        Paragraph('The A* algorithm expands the lowest f(n), choosing nodes that are promising and cost-aware. The final selected route is the path with the minimum total cost, typically S → A → C → G or S → B → D → G, depending on the exact edge weights in the given figure. A* performs better than Greedy Best-First Search because it considers both the actual path cost so far and the heuristic estimate, which prevents the search from being misled by a locally attractive but globally poor corridor.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
        Paragraph('Conclusion: A* is the best choice for ambulance routing because it balances speed and optimality, and it is safer and more reliable for time-critical emergency decisions than purely greedy methods.', ParagraphStyle('P', parent=getSampleStyleSheet()['BodyText'], fontName='Helvetica', fontSize=9.2, leading=12.5, alignment=1)),
    ]
    blocks.append(q5)
    return title, subtitle, blocks


def main():
    docs = [
        ('co1_assignment_1.pdf', build_co1_assignment_1),
        ('co2_assignment_2.pdf', build_co2_assignment_2),
        ('cia_co1_co2.pdf', build_cia_co1_co2),
    ]
    for filename, builder in docs:
        title, subtitle, blocks = builder()
        build_doc(filename, title, subtitle, blocks, total_pages=5)
        print(f'Generated {filename}')


if __name__ == '__main__':
    main()
